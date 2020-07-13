import threading
import sys
import time
import logging
import asyncio
import socket
import json
import pdb  # 7.11
import struct,fcntl # 7.13

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
    SYNCHRONIZE_MSG = 4
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
            log.info("------------")    # 7.11 
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
                log.info("------server handle loop receive------")  #
                send_data = self.handle(recv_msg, conn, addr)  # 7.10
                if send_data:
                    log.info("tcpserver_send:"+send_data)   # 7.10
                    conn.sendall(send_data.encode())        # 7.10
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

    def handle(self, msg, conn, addr):  # 7.10
        code = msg.get("code", 0)
        log.info("code:"+str(code))
        if code == Msg.HAND_SHAKE_MSG:
            log.info("------server receive HAND_SHAKE_MSG------")
            self.handle_handshake(msg, conn, addr)  # 7.10
            res_msg = None  # 7.10
        elif code == Msg.GET_BLOCK_MSG:
            log.info("------server receive GET_BLOCK_MSG------")
            res_msg = self.handle_get_block(msg)
        elif code == Msg.TRANSACTION_MSG:
            log.info("------server receive TRANSACTION_MSG------")
            res_msg = self.handle_transaction(msg)
        elif code == Msg.SYNCHRONIZE_MSG:   # 7.10
            log.info("------server receive SYNCHRONIZE_MSG------")
            self.handle_synchronize(msg, conn, addr)
            res_msg = None
        else:
            return '{"code": 0, "data":""}'

        if res_msg:
            return json.dumps(res_msg.__dict__)
        else:
            return None

    def handle_handshake(self, msg, conn, addr):
        log.info("------server handle_handshake------") # 7.10
        data = msg.get("data", "")
        last_height = data.get("last_height", 0)
        block_chain = BlockChain()
        block = block_chain.get_last_block()

        if block:
            local_last_height = block.block_header.height
        else:
            local_last_height = -1
        log.info("client local_last_height %d, last_height %d" %(local_last_height, last_height))
        
        if local_last_height >= last_height:
            log.info("------server handle_handshake precede------")
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
            send_data = json.dumps(msg.__dict__)
            conn.sendall(send_data.encode())
            log.info("------server handle_handshake precede send msg------")

        elif local_last_height < last_height:
            log.info("------server handle_handshake fall behind------")
            start_height = 0 if local_last_height == -1 else local_last_height
            for i in range(start_height, last_height+1):
                log.info("------server handle_handshake synchronize for------")
                send_msg = Msg(Msg.SYNCHRONIZE_MSG, i)
                send_data = json.dumps(send_msg.__dict__)
                conn.sendall(send_data.encode())
                log.info("------server synchronize already send------")

    def handle_get_block(self, msg):
        log.info("------server handle_get_block------")   # 7.8
        height = msg.get("data", 1)
        block_chain = BlockChain()
        block = block_chain.get_block_by_height(height)
        log.info("------server handle_get_block: get_block_by_height------")   # 7.8
        data = block.serialize()
        msg = Msg(Msg.GET_BLOCK_MSG, data)
        log.info("------server send get_block msg------")   # 7.10
        return msg

    def handle_transaction(self, msg):
        log.info("------server handle_transaction------")    # 7.8
        tx_pool = TxPool()
        txs = msg.get("data", {})
        for tx_data in txs:
            log.info("------server handle_transaction: for------") # 7.8
            tx = Transaction.deserialize(tx_data)
            tx_pool.add(tx)
        if tx_pool.is_full():   # 7.12
            bc = BlockChain()   # 7.12
            bc.add_block(tx_pool.txs)   # 7.12
            log.info("------mine------")   # 7.12
            sleep(1000000000)
            tx_pool.clear() # 7.12
        log.info("------mine------")   # 7.12
        msg = Msg(Msg.NONE_MSG, "")
        return msg

    def handle_synchronize(self, msg, conn, addr):   # 7.10
        data = msg.get("data", "")
        block = Block.deserialize(data)
        bc = BlockChain()
        try:
            bc.add_block_from_peers(block)
            log.info("------server handle_get_block add_block_from_peers------")
            send_data = '{"code": 0, "data":""}'
            conn.sendall(send_data.encode())
        except ValueError as e:
            log.info("------server handle_get_block failed to add_block_from_peers------")
            log.info(str(e))


class TCPClient(object):
    def __init__(self, ip, port):
        self.txs = []
        self.sock = socket.socket()
        self.ip = ip    # 7.11
        self.port = port    # 7.11
        log.info("connect ip:"+ip+"\tport:"+str(port))
        self.sock.connect((ip, port))

    def add_tx(self, tx):
        log.info("------client add_tx------")   # 7.10
        self.txs.append(tx)

    def send(self, msg):
        log.info("------client send------") # 7.10
        data = json.dumps(msg.__dict__)
        self.sock.sendall(data.encode())
        log.info("client send:"+data)
        recv_data = self.sock.recv(4096)
        log.info("client_recv_data:"+str(recv_data))
        try:
            log.info("------client try loads and handle data------")
            # recv_msg = json.loads(str(recv_data))
            recv_msg = eval(recv_data.decode()) # 7.10
            self.handle(recv_msg)  # 7.7 delete str
            log.info("------client had loads and handle data------")    # 7.10
        except json.decoder.JSONDecodeError as e:
            return
        # self.handle(str(recv_msg))  # 7.5

    def handle(self, msg):
        code = msg.get("code", 0)
        log.info("client handle: recv code:"+str(code))
        if code == Msg.HAND_SHAKE_MSG:
            self.handle_shake(msg)
        elif code == Msg.GET_BLOCK_MSG:
            self.handle_get_block(msg)
        elif code == Msg.TRANSACTION_MSG:
            self.handle_transaction(msg)
        elif code == Msg.SYNCHRONIZE_MSG:   # 7.10
            self.handle_synchronize(msg)    # 7.10

    def shake_loop(self):
        # log.info("------'client shake_loop'------") # 7.8
        while True:
            log.info("------client shake_loop ip:"+self.ip+"\tport:"+str(self.port)+"------")   # 7.11
            if self.txs:
                log.info("------client server has txs------")   # 7.10
                sleep(1000000)
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
                time.sleep(1)   # 7.7 10->1


    def handle_shake(self, msg):
        log.info("------client handle_shake------")     # 7.10
        data = msg.get("data", "")
        last_height = data.get("last_height", 0)
        block_chain = BlockChain()
        block = block_chain.get_last_block()
        if block:
            local_last_height = block.block_header.height
        else:
            local_last_height = -1
        log.info("client local_last_height %d, last_height %d" %(local_last_height, last_height))
        if local_last_height > last_height: # pass
            log.info("------error shake------")
            log.info("client local_last_height %d, last_height %d" %(local_last_height, last_height))
        elif local_last_height < last_height:
            start_height = 0 if local_last_height == -1 else local_last_height
            for i in range(start_height, last_height+1):
                log.info("------client handle_shake send block msg------")  # 7.10
                send_msg = Msg(Msg.GET_BLOCK_MSG, i)
                self.send(send_msg)
        # else:   # 7.11
        #     block_chain = BlockChain()
        #     block = block_chain.get_last_block()
        #     try:
        #         genesis_block = block_chain[0]
        #     except IndexError as e:
        #         genesis_block = None
        #     data = {
        #         "last_height": -1,
        #         "genesis_block": ""
        #     }
        #     if genesis_block:
        #         data = {
        #             "last_height": block.block_header.height,
        #             "genesis_block": genesis_block.serialize()
        #         }
        #     msg = Msg(Msg.HAND_SHAKE_MSG, data)
        #     self.send(msg)
        #     time.sleep(30)

    def handle_get_block(self, msg):
        log.info("------client handle_get_block------") # 7.8
        data = msg.get("data", "")
        # log.info("------deserialize these data: " + msg + "------")    # 7.10
        # log.info("------data type" + type(msg) + "------")  # 7.10
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
        if tx_pool.is_full():   # 7.12
            bc.add_block(tx_pool.txs)   # 7.12
            log.info("------mined------")   # 7.12
            sleep(1000000)
            tx_pool.clear() # 7.12
    
    def handle_synchronize(self, msg):  # 7.10
        height = msg.get("data", 1)
        block_chain = BlockChain()
        block = block_chain.get_block_by_height(height)
        data = block.serialize()
        msg = Msg(Msg.SYNCHRONIZE_MSG, data)
        self.send(msg)

    def close(self):
        self.sock.close()


class PeerServer(Singleton):
    def __init__(self):
        if not hasattr(self, "peers"):
            self.peers = []
        if not hasattr(self, "nodes"):
            self.nodes = []
    
    def get_ip(self, ifname='ens33'):   # 7.13
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15],'utf-8')))[20:24])

    def nodes_find(self, p2p_server):
        log.info("------------")  # 7.8 find it very important
        local_ip = self.get_ip() # socket.gethostbyname(socket.getfqdn(socket.gethostname()))
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
        log.info("------peerserver broadcast_tx------")  # 7.10
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
