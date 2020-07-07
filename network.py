# coding:utf-8

import threading
import sys
import time
import logging
import asyncio
import socket
import json

from kademlia.network import Server
from block_chain import BlockChain
from block import Block
from txpool import TxPool
from transactions import Transaction
from utils import Singleton
from conf import bootstrap_host, bootstrap_port, listen_port

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

class P2p(object):
    def __init__(self):
        self.server = Server()
        self.loop = None

    def run(self):
        loop = asyncio.get_event_loop()
        self.loop = loop
        loop.run_until_complete(self.server.listen(listen_port))
        self.loop.run_until_complete(self.server.bootstrap([(bootstrap_host, bootstrap_port)]))
        loop.run_forever()

    def get_nodes(self):
        nodes = []
        for bucket in self.server.protocol.router.buckets:
            nodes.extend(bucket.get_nodes())
        return nodes

class Msg(object):
    NONE_MSG = 0
    HAND_SHAKE_MSG = 1
    GET_BLOCK_MSG = 2
    TRANSACTION_MSG = 3
    def __init__(self, code, data):
        self.code = code
        self.data = data

class TCPServer(object):
    def __init__(self, ip='0.0.0.0', port=listen_port):
        self.sock = socket.socket()
        self.ip = ip
        self.port = port

    def listen(self):
        log.info("---------------'listen' called----------------------")  # net
        self.sock.bind((self.ip, self.port))
        self.sock.listen(125)     # 7.5

    def run(self):
        log.info("---------------'run' called----------------------")  # net
        t = threading.Thread(target=self.listen_loop, args=())
        t.start()

    def handle_loop(self, conn, addr):
        log.info("---------------'handle_loop' called----------------------")  # net
        while True:
            recv_data = conn.recv(4096)
            log.info("recv_data:"+str(recv_data))
            try:
                recv_msg = json.loads(str(recv_data))   # 7.5
                log.info("--------------receive successfully----------------")
                send_data = self.handle(str(recv_msg))  # 7.5
                log.info("tcpserver_send:"+send_data)   # 7.5
                conn.sendall(send_data.encode())        # 7.5
            except ValueError as e:
                conn.sendall('{"code": 0, "data": ""}'.encode())
                log.info("---------------receive unsuccessfully-------------")
            # send_data = self.handle(str(recv_msg))  # 7.5
            # log.info("tcpserver_send:"+send_data)   # 7.5
            # conn.sendall(send_data.encode())        # 7.5

    def listen_loop(self):
        log.info("---------------'listen_loop' called----------------------")  # net
        while True:
            log.info("---------------'while in lp' called----------------------")  # net
            conn, addr = self.sock.accept()
            log.info("--------conn: " + str(conn) + "addr: " + str(addr) + "--------------")
            t = threading.Thread(target=self.handle_loop, args=(conn, addr))
            t.start()

    def handle(self, msg):
        code = msg.get("code", 0)
        log.info("code:"+str(code))
        if code == Msg.HAND_SHAKE_MSG:
            res_msg = self.handle_handshake(msg)    # what to do
        elif code == Msg.GET_BLOCK_MSG:
            res_msg = self.handle_get_block(msg)
        elif code == Msg.TRANSACTION_MSG:
            res_msg = self.handle_transaction(msg)
        else:
            return '{"code": 0, "data":""}'
        return json.dumps(res_msg.__dict__)

    def handle_handshake(self, msg):
        block_chain = BlockChain()
        block = block_chain.get_last_block()
        try:
            genesis_block = block_chain[0]
        except IndexError as e:
            genesis_block = None
        data = {
            "last_height": -1,
            "genesis_block": ""
        }
        if genesis_block:
            data = {
                "last_height": block.block_header.height,
                "genesis_block": genesis_block.serialize()
            }
        msg = Msg(Msg.HAND_SHAKE_MSG, data)
        return msg

    def handle_get_block(self, msg):
        height = msg.get("data", 1)
        block_chain = BlockChain()
        block = block_chain.get_block_by_height(height)
        data = block.serialize()
        msg = Msg(Msg.GET_BLOCK_MSG, data)
        return msg

    def handle_transaction(self, msg):
        tx_pool = TxPool()
        txs = msg.get("data", {})
        for tx_data in txs:
            tx = Transaction.deserialize(tx_data)
            tx_pool.add(tx)
        # if tx_pool.is_full():   # change
            # bc = BlockChain()   # change delete
            # bc.add_block(tx_pool.txs)   # change delete
            # log.info("add block")   # change leave here
            # tx_pool.clear() # wait delete
        # log.info("add block")   # change
        msg = Msg(Msg.NONE_MSG, "")
        return msg


class TCPClient(object):
    def __init__(self, ip, port):
        self.txs = []
        self.sock = socket.socket()
        log.info("connect ip:"+ip+"\tport:"+str(port))
        self.sock.connect((ip, port))

    def add_tx(self, tx):
        self.txs.append(tx)

    def send(self, msg):
        data = json.dumps(msg.__dict__)
        self.sock.sendall(data.encode())
        log.info("send:"+data)
        recv_data = self.sock.recv(4096)
        log.info("client_recv_data:"+str(recv_data))
        try:
            recv_msg = json.loads(str(recv_data))
            self.handle(str(recv_msg))  # 7.5
        except json.decoder.JSONDecodeError as e:
            return
        # self.handle(str(recv_msg))  # 7.5

    def handle(self, msg):
        code = msg.get("code", 0)
        log.info("recv code:"+str(code))
        if code == Msg.HAND_SHAKE_MSG:
            self.handle_shake(msg)
        elif code == Msg.GET_BLOCK_MSG:
            self.handle_get_block(msg)
        elif code == Msg.TRANSACTION_MSG:
            self.handle_transaction(msg)

    def shake_loop(self):
        log.info("---------------'TCPClient shake_loop' called---------------")
        while True:
            if self.txs:
                data = [tx.serialize() for tx in self.txs]
                msg = Msg(Msg.TRANSACTION_MSG, data)
                self.send(msg)
                self.txs.clear()
            else:
                log.info("shake")
                block_chain = BlockChain()
                block = block_chain.get_last_block()
                try:
                    genesis_block = block_chain[0]
                except IndexError as e:
                    genesis_block = None
                data = {
                    "last_height": -1,
                    "genesis_block": ""
                }
                if genesis_block:
                    data = {
                        "last_height": block.block_header.height,
                        "genesis_block": genesis_block.serialize()
                    }
                msg = Msg(Msg.HAND_SHAKE_MSG, data)
                self.send(msg)
                time.sleep(10)


    def handle_shake(self, msg):
        data = msg.get("data", "")
        last_height = data.get("last_height", 0)
        block_chain = BlockChain()
        block = block_chain.get_last_block()
        if block:
            local_last_height = block.block_header.height
        else:
            local_last_height = -1
        log.info("local_last_height %d, last_height %d" %(local_last_height, last_height))
        if local_last_height >= last_height:
            return
        start_height = 0 if local_last_height == -1 else local_last_height
        for i in range(start_height, last_height+1):
            send_msg = Msg(Msg.GET_BLOCK_MSG, i)
            self.send(send_msg)

    def handle_get_block(self, msg):
        data = msg.get("data", "")
        block = Block.deserialize(data)
        bc = BlockChain()
        try:
            bc.add_block_from_peers(block)
        except ValueError as e:
            log.info(str(e))

    def handle_transaction(self, msg):
        data = msg.get("data", {})
        tx = Transaction.deserialize(data)
        tx_pool = TxPool()
        tx_pool.add(tx)
        # if tx_pool.is_full():   # change
            # bc.add_block(tx_pool.txs)   # change
            # log.info("mined a block")   # change
            # tx_pool.clear() # change
    def close(self):
        self.sock.close()


class PeerServer(Singleton):
    def __init__(self):
        if not hasattr(self, "peers"):
            self.peers = []
        if not hasattr(self, "nodes"):
            self.nodes = []

    def nodes_find(self, p2p_server):
        log.info("---------------'PeerServer nodes_find called-----------------'")
        local_ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
        while True:
            nodes = p2p_server.get_nodes()
            log.info("-------------------------get_nodes called-----s--------------------------")
            for node in nodes:
                if node not in self.nodes:
                    ip = node.ip
                    port = node.port
                    if local_ip == ip:
                        continue
                    log.info("------------will call PeerServer nodes_find-----------")
                    client = TCPClient(ip, port)
                    log.info("-------------PeerServer nodes_find called-------------")
                    t = threading.Thread(target=client.shake_loop, args=())
                    t.start()
                    self.peers.append(client)
                    self.nodes.append(node)
            time.sleep(1)

    def broadcast_tx(self, tx):
        for peer in self.peers:
            peer.add_tx(tx)

    def run(self, p2p_server):
        log.info("---------------PeerServer run called-------------------------")
        t = threading.Thread(target=self.nodes_find, args=(p2p_server,))
        t.start()

if __name__ == "__main__":
    tcpserver = TCPServer()
    tcpserver.listen()
    tcpserver.run()

    p2p = P2p()
    server = PeerServer()
    server.run(p2p)
    p2p.run()
