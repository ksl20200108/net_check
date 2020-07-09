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
        log.info("------------") # 7.8 find it also important
        nodes = []
        for bucket in self.server.protocol.router.buckets:
            # log.info("------int the for------")    # 7.8
            nodes.extend(bucket.get_nodes())
        # log.info("------will return nodes------")   # 7.8
        return nodes

class Msg(object):
    NONE_MSG = 0
    HAND_SHAKE_MSG = 1
    GET_BLOCK_MSG = 2
    TRANSACTION_MSG = 3
    SEND_BLOCK_MSG = 4  # 7.9
    def __init__(self, code, data):
        self.code = code
        self.data = data


class TCPServer(object):
    def __init__(self, ip='0.0.0.0', port=listen_port):
        self.sock = socket.socket()
        self.ip = ip
        self.port = port

    def listen(self):
        # log.info("'listen' called")  # 7.8
        self.sock.bind((self.ip, self.port))
        self.sock.listen(125)     # 7.5

    def run(self):
        # log.info("'run' called")  # 7.8
        t = threading.Thread(target=self.listen_loop, args=())
        t.start()

    def handle_loop(self, conn, addr):
        # log.info("------'handle_loop' called------")  # 7.8
        while True:
            recv_data = conn.recv(4096)
            # log.info("recv_data:"+str(recv_data)[1:])   # 7.8
            # log.info("and the bytes are: " + recv_data.decode()) # 7.8
            if not recv_data:   # 7.7
                continue    # 7.7
            try:
                # log.info("-----in try json loads these data: " + str(recv_data))    # 7.8
                try:
                    recv_msg = eval(recv_data.decode())   # 7.7
                except:
                    log.info("------the null data is" + str(recv_data) + "------") # 7.7
                # try:  # 7.7
                #     recv_msg = json.loads(recv_data.decode()) # 7.7
                # log.info("the type is "+ str(type(recv_msg))) # 7.8
                log.info("------server handle loop receive------")  # 7.9
                send_data = self.handle(recv_msg)  # 7.7
                log.info("tcpserver_send:"+send_data)   # 7.5
                conn.sendall(send_data.encode())        # 7.5
            except ValueError as e:
                conn.sendall('{"code": 0, "data": ""}'.encode())
                log.info("------receive Unsuccessfully------")
            # send_data = self.handle(str(recv_msg))  # 7.5
            # log.info("tcpserver_send:"+send_data)   # 7.5
            # conn.sendall(send_data.encode())        # 7.5

    def listen_loop(self):
        # log.info("------'listen_loop' called------")  # 7.8
        while True:
            # log.info("------'while in lp' called------")  # 7.8
            conn, addr = self.sock.accept()
            log.info("--------conn: " + str(conn) + "addr: " + str(addr) + "--------------")
            t = threading.Thread(target=self.handle_loop, args=(conn, addr))
            t.start()

    def handle(self, msg):
        # log.info("------tcpserver handle msg------")  # 7.8
        code = msg.get("code", 0)
        log.info("code:"+str(code))
        if code == Msg.HAND_SHAKE_MSG:
            res_msg = self.handle_handshake(msg)    # what to do
        elif code == Msg.GET_BLOCK_MSG:
            log.info("------receive GET_BLOCK_MSG------")   # 7.8
            res_msg = self.handle_get_block(msg)
        elif code == Msg.TRANSACTION_MSG:
            log.info("------receive TRANSACTION_GSG------") # 7.8
            res_msg = self.handle_transaction(msg)
        elif code == Msg.SEND_BLOCK_MSG:    # 7.9
            pass    # 7.9
        else:
            return '{"code": 0, "data":""}'
        return json.dumps(res_msg.__dict__)

    def handle_handshake(self, msg):    # 78pm problem
        log.info("------server handle_handshake------") # 78pm
        data = msg.get("data", "")  # 7.9
        last_height = data.get("last_height", 0)    # 7.9
        block_chain = BlockChain()
        block = block_chain.get_last_block()
        # try:                                              # 7.9
        #     genesis_block = block_chain[0]                # 7.9
        # except IndexError as e:                           # 7.9
        #     genesis_block = None                          # 7.9
        # data = {                                          # 7.9
        #     "last_height": -1,                            # 7.9
        #     "genesis_block": ""                           # 7.9
        # }                                                 # 7.9
        # if genesis_block:                                 # 7.9
        #     data = {                                      # 7.9
        #         "last_height": block.block_header.height,  # 7.9
        #         "genesis_block": genesis_block.serialize()  # 7.9
        #     }                                             # 7.9
        if block:                                           # 7.9
            local_last_height = block.block_header.height   # 7.9
        else:                                               # 7.9
            local_last_height = -1                          # 7.9
        log.info("local_last_height %d, last_height %d" %(local_last_height, last_height))  # 7.9
        if local_last_height >= last_height:                # 7.9
            return                                          # 7.9
        start_height = 0 if local_last_height == -1 else local_last_height                  # 7.9
        for i in range(start_height, last_height+1):        # 7.9
            log.info("------client handle_shake send block msg------")                      # 7.9
            send_msg = Msg(Msg.GET_BLOCK_MSG, i)            # 7.9
            self.send(send_msg)                             # 7.9
        # msg = Msg(Msg.GET_BLOCK_MSG, data)  # 7.9
        log.info("------server send get_block_msg------")   # 78pm
        # conn.sendall(json.dumps(Msg(Msg.HAND_SHAKE_MSG, data).__dict__).encode())        # 78pm
        return msg

    def handle_get_block(self, msg):
        log.info("------into server handle_get_block------")   # 7.8
        height = msg.get("data", 1)
        block_chain = BlockChain()
        block = block_chain.get_block_by_height(height)
        log.info("------server handle_get_block: get_block_by_height------")   # 7.8
        data = block.serialize()
        msg = Msg(Msg.GET_BLOCK_MSG, data)
        return msg

    def handle_transaction(self, msg):
        log.info("------into server handel _transaction------")    # 7.8
        tx_pool = TxPool()
        txs = msg.get("data", {})
        for tx_data in txs:
            log.info("------server handle_transaction: for------") # 7.8
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
    
    def handle_send_block(self, msg):   # 7.9
        pass    # 7.9


class TCPClient(object):
    def __init__(self, ip, port):
        self.txs = []
        self.sock = socket.socket()
        log.info("connect ip:"+ip+"\tport:"+str(port))
        self.sock.connect((ip, port))

    def add_tx(self, tx):
        log.info("------client add_tx------")   # 78pm
        self.txs.append(tx)

    def send(self, msg):
        data = json.dumps(msg.__dict__)
        self.sock.sendall(data.encode())
        log.info("send:"+data)
        recv_data = self.sock.recv(4096)
        log.info("client_recv_data:"+str(recv_data))
        try:
            log.info("------client try loads and handle data------")    # 78pm
            # recv_msg = json.loads(str(recv_data)) # 7.9
            recv_msg = eval(recv_data.decode()) # 7.9
            self.handle(recv_msg)  # 7.7 delete str
            log.info("------client had loads and handle data------")
        except json.decoder.JSONDecodeError as e:
            return
        # self.handle(str(recv_msg))  # 7.5

    def handle(self, msg):
        code = msg.get("client handle: msg code", 0)
        log.info("client handle: recv code:"+str(code))
        if code == Msg.HAND_SHAKE_MSG:
            self.handle_shake(msg)
        elif code == Msg.GET_BLOCK_MSG:
            self.handle_get_block(msg)
        elif code == Msg.TRANSACTION_MSG:
            self.handle_transaction(msg)
        elif code == Msg.SEND_BLOCK_MSG:    # 7.9
            pass    # 7.9

    def shake_loop(self):
        # log.info("------'client shake_loop'------") # 7.8
        while True:
            if self.txs:
                log.info("------client server has txs------")   # 78pm
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
                msg = Msg(Msg.HAND_SHAKE_MSG, data) # 78pm
                self.send(msg)
                time.sleep(1)   # 7.7 10->1


    def handle_shake(self, msg):
        log.info("------client handle_shake------") # 78pm
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
            log.info("------client handle_shake send block msg------")  # 78pm
            send_msg = Msg(Msg.GET_BLOCK_MSG, i)    # 78pm but unchanged
            self.send(send_msg)

    def handle_get_block(self, msg):
        log.info("------client handle_get_block------") # 7.8
        data = msg.get("data", "")
        log.info("------deserialize these data: " + msg + "------")    # 7.9
        log.info("------data type" + type(msg) + "------")  # 7.9
        block = Block.deserialize(data)
        bc = BlockChain()
        try:
            bc.add_block_from_peers(block)
            log.info("------client handle_get_block add_block_from_peers------")    # 7.8
        except ValueError as e:
            log.info("------client handle_get_block failed to add_block_from_peers------")  # 7.8
            log.info(str(e))

    def handle_transaction(self, msg):
        log.info("------client handle_transaction------")   # 7.8
        data = msg.get("data", {})
        tx = Transaction.deserialize(data)
        tx_pool = TxPool()
        tx_pool.add(tx)
        log.info("------client handel_transaction txpool added------")  # 7.8
        # if tx_pool.is_full():   # change
            # bc.add_block(tx_pool.txs)   # change
            # log.info("mined a block")   # change
            # tx_pool.clear() # change
    
    def handle_send_block(self, msg):   # 7.9
        pass    # 7.9
    
    def close(self):
        self.sock.close()


class PeerServer(Singleton):
    def __init__(self):
        if not hasattr(self, "peers"):
            self.peers = []
        if not hasattr(self, "nodes"):
            self.nodes = []

    def nodes_find(self, p2p_server):
        log.info("------------")  # 7.8 find it very important
        local_ip = "192.168.57.129" # socket.gethostbyname(socket.getfqdn(socket.gethostname()))
        while True:
            nodes = p2p_server.get_nodes()
            log.info("-------------")     # 7.8 find it very important
            for node in nodes:
                if node not in self.nodes:
                    # log.info("------------nodes ip: " + node.ip + "------------")   # 7.8
                    ip = node.ip
                    port = node.port
                    if local_ip == ip:
                        # log.info("------local_ip==ip------")  # 7.8
                        continue
                    log.info("------------nodes ip: " + node.ip + "------------")   # 7.8
                    # log.info("------will call PeerServer nodes_find------")   # 7.8
                    client = TCPClient(ip, port)
                    # log.info("------PeerServer nodes_find called------")  # 7.8
                    t = threading.Thread(target=client.shake_loop, args=())
                    t.start()
                    self.peers.append(client)
                    self.nodes.append(node)
            time.sleep(1)

    def broadcast_tx(self, tx):
        log.info("------peerserver broadcast_tx------")  # 78pm
        for peer in self.peers:
            peer.add_tx(tx)

    def run(self, p2p_server):
        # log.info("------PeerServer run called------")   # 7.8
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
