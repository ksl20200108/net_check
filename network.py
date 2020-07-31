import threading
import sys
import time
import logging
import asyncio
import socket
import json
import pdb  # 7.11
import random
import socket, struct, fcntl

from kademlia.network import Server
from block_chain import BlockChain
from block import Block
from txpool import TxPool
from transactions import Transaction
from utils import Singleton
from conf import bootstrap_host, bootstrap_port, listen_port
from signal import signal, SIGPIPE, SIG_DFL  # 7.23

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

# signal(SIGPIPE,SIG_DFL) # 7.23

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
        log.info("------------")  # 7.8 find it also important
        nodes = []
        if self.server.protocol:  # 7.18
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
    MISS_TRANSACTION_MSG = 5  # 7.21
    GET_TRANSACTION_MSG = 6   # 7.21

    def __init__(self, code, data):
        self.code = code
        self.data = data


class TCPServer(object):
    def __init__(self, ip='0.0.0.0', port=listen_port):
        self.sock = socket.socket()
        self.ip = ip
        self.port = port

    def listen(self):
        self.sock.bind((self.ip, self.port))
        self.sock.listen(125)  # 7.5

    def run(self):
        t = threading.Thread(target=self.listen_loop, args=())
        t.start()

    def handle_loop(self, conn, addr):
        while True:
            log.info("------s handle loop------")  # 7.11
            header_size = struct.unpack('i', conn.recv(4))[0]
            header_bytes = conn.recv(header_size)
            header = eval(header_bytes.decode())
            send_size = header["send_size"]
            recv_size = 0
            recv_data = b''
            while recv_size < send_size:
                res = conn.recv(1024)
                recv_data += res
                recv_size += len(res)
            # recv_data = conn.recv(send_size)    # 7.21
            log.info("------server handle_loop recv_data:" + str(recv_data)[1:] + "------")   # 7.8
            if not recv_data:  # 7.7
                log.info("------server handle_loop connection broke------")
                continue    # 7.19
            try:
                # log.info("-----in try json loads these data: " + str(recv_data))    # 7.8
                try:
                    recv_msg = eval(recv_data.decode())  # 7.7
                except:
                    log.info("------server the null data is" + str(recv_data) + "------")  # 7.7

                log.info("------server handle loop receive------")
                send_data = self.handle(recv_msg, conn, addr)  # 7.10
                # time.sleep(1)
                # if send_data:
                log.info("tcpserver_send:" + send_data)  # 7.10
                log.info("------data send to: " + str(addr) + "------")  # 7.21
                send_bytes = send_data.encode()
                header_json = json.dumps({"send_size": len(send_bytes)})
                header_bytes = header_json.encode()
                header_size = len(header_bytes)
                conn.sendall(struct.pack('i', header_size))
                conn.sendall(header_bytes)
                conn.sendall(send_bytes)  # 7.10
            except ValueError as e:
                # time.sleep(1)
                send_data = json.dumps(Msg(Msg.NONE_MSG, "").__dict__)  # 7.23
                send_bytes = send_data.encode()
                header_json = json.dumps({"send_size": len(send_bytes)})
                header_bytes = header_json.encode()
                header_size = len(header_bytes)
                conn.sendall(struct.pack('i', header_size))
                conn.sendall(header_bytes)
                conn.sendall(send_bytes)  # '{"code": 0, "data": ""}' # 7.23
                log.info("------receive Unsuccessfully------")

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
        log.info("code:" + str(code))
        if code == Msg.HAND_SHAKE_MSG:
            log.info("------server receive HAND_SHAKE_MSG------")
            res_msg = self.handle_handshake(msg, conn, addr)  # 7.10
            # res_msg = None  # 7.10
        elif code == Msg.GET_BLOCK_MSG:
            log.info("------server receive GET_BLOCK_MSG------")
            res_msg = self.handle_get_block(msg, conn, addr)
        elif code == Msg.TRANSACTION_MSG:
            log.info("------server receive TRANSACTION_MSG------")
            res_msg = self.handle_transaction(msg, conn, addr)  # 7.20
        elif code == Msg.SYNCHRONIZE_MSG:  # 7.10
            log.info("------server receive SYNCHRONIZE_MSG------")
            res_msg = self.handle_synchronize(msg, conn, addr)
            # res_msg = None
        elif code == Msg.MISS_TRANSACTION_MSG:  # 7.21
            log.info("------server receive MISS_TRANSACTION_MSG------")
            res_msg = self.handle_miss(msg, conn, addr)
        else:
            return json.dumps(Msg(Msg.NONE_MSG, "").__dict__)    # '{"code": 0, "data":""}'    # 7.23

        if res_msg:
            return json.dumps(res_msg.__dict__)
        else:
            return json.dumps(Msg(Msg.NONE_MSG, "").__dict__)   # 7.23

    def handle_handshake(self, msg, conn, addr):
        log.info("------server handle_handshake from " + str(addr) + "------")  # 7.10
        data = msg.get("data", "")
        last_height = data.get("last_height", 0)
        log.info("------with last_height " + str(last_height) + "------")
        block_chain = BlockChain()
        block = block_chain.get_last_block()

        if block:
            local_last_height = block.block_header.height
        else:
            local_last_height = -1
        log.info("server local_last_height %d, last_height %d" % (local_last_height, last_height))

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
                    "last_height": local_last_height,
                    "genesis_block": genesis_block.serialize()
                }
            msg = Msg(Msg.HAND_SHAKE_MSG, data)
            return msg
            # send_data = json.dumps(msg.__dict__)
            # time.sleep(1)  # 7.13
            # send_bytes = send_data.encode()
            # header_json = json.dumps({"send_size": len(send_bytes)})
            # header_bytes = header_json.encode()
            # header_size = len(header_bytes)
            # conn.sendall(struct.pack('i', header_size))
            # conn.sendall(header_bytes)
            # conn.sendall(send_bytes)
            # log.info("------server handle_handshake precede send msg: " + str(data) + "------")

        elif local_last_height < last_height:
            log.info("------server handle_handshake fall behind------")
            start_height = 0 if local_last_height == -1 else local_last_height
            synchronize_range = [start_height, last_height+1]
            send_msg = Msg(Msg.SYNCHRONIZE_MSG, synchronize_range)
            return send_msg
            # send_data = json.dumps(send_msg.__dict__)
            # send_bytes = send_data.encode()
            # header_json = json.dumps({"send_size": len(send_bytes)})
            # header_bytes = header_json.encode()
            # header_size = len(header_bytes)
            # conn.sendall(struct.pack('i', header_size))
            # conn.sendall(header_bytes)
            # conn.sendall(send_bytes)
            # log.info("------server synchronize already send------")

            # for i in range(start_height, last_height + 1):
            #     log.info("------server handle_handshake synchronize for------")
            #     send_msg = Msg(Msg.SYNCHRONIZE_MSG, i)
            #     send_data = json.dumps(send_msg.__dict__)
            #     send_bytes = send_data.encode()
            #     header_json = json.dumps({"send_size": len(send_bytes)})
            #     header_bytes = header_json.encode()
            #     header_size = len(header_bytes)
            #     conn.sendall(struct.pack('i', header_size))
            #     conn.sendall(header_bytes)
            #     conn.sendall(send_bytes)
            #     log.info("------server synchronize already send------")

    def handle_get_block(self, msg, conn, addr):
        log.info("------server handle_get_block from " + str(addr) + "------")  # 7.8
        get_range = msg.get("data", 1)
        log.info("------with range " + str(get_range[0]) + " " + str(get_range[1]) + "------")
        block_chain = BlockChain()
        data = []
        for height in range(get_range[0], get_range[1]):
            already_get = False
            for i in range(0, 2):
                block = None
                try:
                    block = block_chain.get_block_by_height(height)
                except:
                    continue
                if block:
                    already_get = True
                    break
            if already_get:
                block = block.serialize()
                data.append(block)
            elif data:
                msg = Msg(Msg.GET_BLOCK_MSG, data)
                log.info("------server send get_block msg------")  # 7.10
                return msg
            else:
                msg = Msg(Msg.NONE_MSG, "")
                return msg
        log.info("------server handle_get_block: get_block_by_height------")  # 7.8
        # data = block.serialize()
        msg = Msg(Msg.GET_BLOCK_MSG, data)
        log.info("------server send get_block msg------")  # 7.10
        return msg

    def handle_transaction(self, msg, conn, addr):  # 7.20
        log.info("------server handle_transaction------")  # 7.8
        tx_pool = TxPool()
        txs = msg.get("data", {})
        for tx_data in txs:
            log.info("------server handle_transaction: for------")  # 7.8
            tx = Transaction.deserialize(tx_data)
            is_new = True
            if tx_pool.is_new(tx):  # 7.20
                log.info("------server never get this transaction before------")  # 7.20
                bc = BlockChain()
                ls_bl = bc.get_last_block()
                if ls_bl:
                    ls_height = ls_bl.block_header.height
                    for i in range(0, ls_height + 1):
                        while True:
                            block = None
                            try:
                                block = bc.get_block_by_height(i)
                            except:
                                continue
                            if block:
                                break
                        bc_txs = block._transactions
                        if bc_txs:
                            for transaction in bc_txs:
                                if transaction.txid == tx.txid:
                                    log.info("------old transaction------")
                                    log.info("------the id is: " + str(tx.txid) + "------")  # 7.20
                                    is_new = False
                                    # break
                                else:
                                    log.info("------brand new------")
                                    log.info("------the id is: " + str(tx.txid) + "------")  # 7.20
                        if not is_new:
                            break
                if is_new:
                    tx_pool.add(tx)
                    log.info("------server add this transaction------")
                    log.info("------the id is: " + str(tx.txid) + "------")
                    server1 = PeerServer()
                    server1.broadcast_tx(tx)
                    log.info("------server handle_transaction broadcast------")
        msg = Msg(Msg.NONE_MSG, "")
        return msg

    def handle_synchronize(self, msg, conn, addr):  # 7.10
        datas = msg.get("data", "")
        log.info("------s handle_synchronize from " + str(addr) + "------")
        log.info("------with data " + str(datas) + "------")
        # block = Block.deserialize(data)
        bc = BlockChain()
        try:
            ls_blo = bc.get_last_block()
            if ls_blo:
                # log.info("s handle_synchronize with local last height and last height " + str(ls_blo.block_header.height) + " " + str(block.block_header.height))
                for data in datas:
                    block = Block.deserialize(data)
                    if block.block_header.height > ls_blo.block_header.height: 
                        bc.add_block_from_peers(block)
                        log.info("------server handle_get_block add_block_from_peers------")
                    else:
                        log.info("------error add------")
            else:
                for data in datas:
                    block = Block.deserialize(data)
                    try:
                        bc.add_block_from_peers(block)
                        log.info("------server handle_get_block add_block_from_peers------")
                    except:
                        pass
            msg = Msg(Msg.NONE_MSG, "")
            return msg
            # send_data = json.dumps(Msg(Msg.NONE_MSG, "").__dict__) # '{"code": 0, "data":""}'    # pass
            # send_bytes = send_data.encode()
            # header_json = json.dumps({"send_size": len(send_bytes)})
            # header_bytes = header_json.encode()
            # header_size = len(header_bytes)
            # conn.sendall(struct.pack('i', header_size))
            # conn.sendall(header_bytes)
            # conn.sendall(send_bytes)
        except ValueError as e:
            log.info("------server handle_get_block failed get last block------")
            log.info(str(e))
            msg = Msg(Msg.NONE_MSG, "")
            return msg

    def handle_miss(self, msg, conn, addr):  # 7.21
        log.info("------server handle miss------")
        data = msg.get("data", "")
        tx_pool1 = TxPool()
        log.info("------server tx: " + str(len(tx_pool1.pre_txs)) + "client tx: " + str(int(data)) + "------")
        if len(tx_pool1.pre_txs) < int(data):
            log.info("------shorter------")
            msg = Msg(Msg.GET_TRANSACTION_MSG, "")
            return msg
        elif len(tx_pool1.pre_txs) > int(data):
            log.info("------longer------")
            data = [tx.serialize() for tx in tx_pool1.txs]
            msg = Msg(Msg.MISS_TRANSACTION_MSG, data)
            return msg
        else:
            log.info("------the same------")
            msg = Msg(Msg.NONE_MSG, "")
            return msg


class TCPClient(object):
    def __init__(self, ip, port):
        self.txs = []
        self.sock = socket.socket()
        self.ip = ip  # 7.11
        self.port = port  # 7.11
        log.info("connect ip:" + ip + "\tport:" + str(port))
        self.sock.connect((ip, port))

    def add_tx(self, tx):
        log.info("------client add_tx------")  # 7.10
        self.txs.append(tx)

    def send(self, msg):
        log.info("------client send------")  # 7.10
        data = json.dumps(msg.__dict__)
        send_bytes = data.encode()
        header_json = json.dumps({"send_size": len(send_bytes)})
        header_bytes = header_json.encode()
        header_size = len(header_bytes)
        time.sleep(1)
        self.sock.sendall(struct.pack('i', header_size))
        self.sock.sendall(header_bytes)
        self.sock.sendall(send_bytes)
        log.info("client send to:" + self.ip + "------with these data" + data)
        header_size = struct.unpack('i', self.sock.recv(4))[0]
        header_bytes = self.sock.recv(header_size)
        header = eval(header_bytes.decode())
        send_size = header["send_size"]
        recv_size = 0
        recv_data = b''
        while recv_size < send_size:
            res = self.sock.recv(1024)
            recv_data += res
            recv_size += len(res)
        # recv_data = self.sock.recv(send_size)    # 7.21
        log.info("client_recv_data from:" + self.ip + "------with these data" + str(recv_data))
        try:
            log.info("------client try loads and handle data------")
            # recv_msg = json.loads(str(recv_data))
            recv_msg = eval(recv_data.decode())  # 7.10
            self.handle(recv_msg)  # 7.7 delete str
            log.info("------client had loads and handle data------")  # 7.10
        except:
            return

    def handle(self, msg):
        code = msg.get("code", 0)
        log.info("client handle: recv code:" + str(code))
        if code == Msg.HAND_SHAKE_MSG:
            self.handle_shake(msg)
        elif code == Msg.GET_BLOCK_MSG:
            self.handle_get_block(msg)
        elif code == Msg.TRANSACTION_MSG:
            self.handle_transaction(msg)
        elif code == Msg.SYNCHRONIZE_MSG:  # 7.10
            self.handle_synchronize(msg)  # 7.10
        elif code == Msg.GET_TRANSACTION_MSG:  # 7.21
            self.handle_get_transaction(msg)
        elif code == Msg.MISS_TRANSACTION_MSG:  # 7.21
            self.handle_miss(msg)

    def shake_loop(self):
        # log.info("------'client shake_loop'------") # 7.8
        while True:
            log.info("------client shake_loop ip:" + self.ip + "\tport:" + str(self.port) + "------")  # 7.11
            tx_pool1 = TxPool()  # 7.2
            if self.txs:
                log.info("------client server has txs------")  # 7.10
                data = [tx.serialize() for tx in self.txs]
                log.info("------client serialize transaction-------")
                msg = Msg(Msg.TRANSACTION_MSG, data)
                self.send(msg)
                self.txs = []  # 7.21 'clear' -> '= []'
            elif tx_pool1.pre_txs:
                a = random.uniform(0, 1)
                if a < 0.5:
                    log.info("------has previous transaction------")
                    data = len(tx_pool1.pre_txs)
                    msg = Msg(Msg.MISS_TRANSACTION_MSG, data)
                    self.send(msg)
                else:
                    log.info("shake")
                    block_chain = BlockChain()
                    block = block_chain.get_last_block()
                    try:
                        genesis_block = block_chain[0]
                    except IndexError as e:
                        genesis_block = None
                    if block:
                        last_height = block.block_header.height
                    else:
                        last_height = -1
                    data = {
                        "last_height": -1,
                        "genesis_block": ""
                    }
                    if genesis_block:
                        data = {
                            "last_height": last_height,
                            "genesis_block": genesis_block.serialize()
                        }
                    msg = Msg(Msg.HAND_SHAKE_MSG, data)
                    self.send(msg)
            else:
                log.info("shake")
                block_chain = BlockChain()
                block = block_chain.get_last_block()
                try:
                    genesis_block = block_chain[0]
                except IndexError as e:
                    genesis_block = None
                if block:
                    last_height = block.block_header.height
                else:
                    last_height = -1
                data = {
                    "last_height": -1,
                    "genesis_block": ""
                }
                if genesis_block:
                    data = {
                        "last_height": last_height,
                        "genesis_block": genesis_block.serialize()
                    }
                msg = Msg(Msg.HAND_SHAKE_MSG, data)
                self.send(msg)

    def handle_shake(self, msg):
        log.info("------client handle_shake from " + str(self.ip) + "------")  # 7.10
        data = msg.get("data", "")
        last_height = data.get("last_height", 0)
        log.info("------with last height " + str(last_height) + "------")
        block_chain = BlockChain()
        block = block_chain.get_last_block()
        if block:
            local_last_height = block.block_header.height
        else:
            local_last_height = -1
        log.info("client local_last_height %d, last_height %d" % (local_last_height, last_height))
        if local_last_height > last_height:  # pass
            log.info("------error shake------")
            log.info("client local_last_height %d, last_height %d" % (local_last_height, last_height))
            send_data = []
            for i in range(last_height+1, local_last_height+1):
                already_get = False
                for i in range(0, 2):
                    block = None
                    try:
                        block = block_chain.get_block_by_height(i)
                    except:
                        continue
                    if block:
                        already_get = True
                        break
                if already_get:
                    send_data.append(block.serialize())
                elif send_data:
                    msg = Msg(Msg.SYNCHRONIZE_MSG, send_data)
                    self.send(msg)
                    return
                else:
                    msg = Msg(Msg.NONE_MSG, "")
                    self.send(msg)
                    return
                # send_data = block.serialize()
                msg = Msg(Msg.SYNCHRONIZE_MSG, send_data)
                self.send(msg)
                log.info("------client handle_shake send synchronize msg to" + str(self.ip) + "------")
        elif local_last_height < last_height:
            start_height = 0 if local_last_height == -1 else local_last_height
            # for i in range(start_height, last_height + 1):
            #     log.info("------client handle_shake send block msg------")  # 7.10
            #     send_msg = Msg(Msg.GET_BLOCK_MSG, i)
            #     self.send(send_msg)
            get_range = [start_height, local_last_height+1]
            send_msg = Msg(Msg.GET_BLOCK_MSG, get_range)
            self.send(send_msg)
        else:
            send_msg = Msg(Msg.NONE_MSG, "")
            self.send(send_msg)

    def handle_get_block(self, msg):
        datas = msg.get("data", "")
        log.info("------client handle_get_block from " + str(self.ip) + "------")  # 7.8
        log.info("------with data " + str(datas) + "------")
        # log.info("------deserialize these data: " + msg + "------")    # 7.10
        # log.info("------data type" + type(msg) + "------")  # 7.10
        # block = Block.deserialize(data)
        bc = BlockChain()
        log.info("------client deserialize block from peer------")
        try:
            ls_blo = bc.get_last_block()
            if ls_blo:
                for data in datas:
                    block = Block.deserialize(data)
                    log.info("c handle_get_block local last height and last height " + str(ls_blo.block_header.height) + " " + str(block.block_header.height))
                    if block.block_header.height > ls_blo.block_header.height:
                        bc.add_block_from_peers(block)
                        log.info("------client handle_get_block add_block_from_peers------")  # 7.8
                    else:
                        log.info("------error add as last height " + str(block.block_header.height) + "------")
            else:
                for data in datas:
                    block = Block.deserialize(data)
                    bc.add_block_from_peers(block)
                    log.info("------client handle_get_block add_block_from_peers------")
            msg = Msg(Msg.NONE_MSG, "")
            self.send(msg)
        except ValueError as e:
            log.info("------client handle_get_block failed to add_block_from_peers------")  # 7.8
            log.info(str(e))
            msg = Msg(Msg.NONE_MSG, "")
            self.send(msg)

    def handle_transaction(self, msg):
        log.info("------client handle_transaction------")  # 7.8
        data = msg.get("data", {})
        tx = Transaction.deserialize(data)
        tx_pool = TxPool()
        is_new = True  # 7.20
        if tx_pool.is_new(tx):
            log.info("------client never get this transaction before------")  # 7.20
            bc = BlockChain()
            ls_bl = bc.get_last_block()
            if ls_bl:
                ls_height = ls_bl.block_header.height
                for i in range(0, ls_height + 1):
                    while True:
                        block = None
                        try:
                            block = bc.get_block_by_height(i)
                        except:
                            continue
                        if block:
                            break
                    bc_txs = block._transactions
                    for transaction in bc_txs:
                        if transaction.txid == tx.txid:
                            is_new = False
                            break
                    if not is_new:
                        break
            if is_new:
                tx_pool.add(tx)
                log.info("------client handel_transaction txpool added------")  # 7.8
                server2 = PeerServer()
                server2.broadcast_tx(tx)
                log.info("------client handle_transaction broadcast------")

        msg = Msg(Msg.NONE_MSG, "") # 7.23
        self.send(msg)  # 7.23

    def handle_synchronize(self, msg):  # 7.10
        synchronize_range = msg.get("data", 1)
        block_chain = BlockChain()
        data = []
        for height in range(synchronize_range[0], synchronize_range[1]):
            already_get = False
            for i in range(0, 2):
                block = None
                try:
                    block = block_chain.get_block_by_height(height)
                except:
                    continue
                if block:
                    already_get = True
                    break
            if already_get:
                data.append(block.serialize())
            elif data:
                msg = Msg(Msg.SYNCHRONIZE_MSG, data)
                self.send(msg)
                return
            else:
                msg = Msg(Msg.NONE_MSG, "")
                self.send(msg)
                return
        msg = Msg(Msg.SYNCHRONIZE_MSG, data)
        self.send(msg)

    def handle_get_transaction(self, msg):  # 7.21
        log.info("------client handle_get_transaction------")
        tx_pool1 = TxPool()
        data = [tx.serialize() for tx in tx_pool1.txs]
        msg = Msg(Msg.TRANSACTION_MSG, data)
        self.send(msg)

    def handle_miss(self, msg):  # 7.21
        log.info("------client handle_miss------")
        tx_pool = TxPool()
        txs = msg.get("data", {})
        for tx_data in txs:
            log.info("------server handle_miss: for------")  # 7.8
            tx = Transaction.deserialize(tx_data)
            is_new = True
            if tx_pool.is_new(tx):  # 7.20
                log.info("------client miss this transaction before------")  # 7.20
                bc = BlockChain()
                ls_bl = bc.get_last_block()
                if ls_bl:
                    ls_height = ls_bl.block_header.height
                    for i in range(0, ls_height + 1):
                        while True:
                            block = None
                            try:
                                block = bc.get_block_by_height(i)
                            except:
                                continue
                            if block:
                                break
                        bc_txs = block._transactions
                        if bc_txs:
                            for transaction in bc_txs:
                                if transaction.txid == tx.txid:
                                    log.info("------old transaction------")
                                    log.info("------the id is: " + str(tx.txid) + "------")  # 7.20
                                    is_new = False
                                    # break
                                else:
                                    log.info("------brand new miss------")
                                    log.info("------the id is: " + str(tx.txid) + "------")  # 7.20
                        if not is_new:
                            break
                if is_new:
                    tx_pool.add(tx)
                    log.info("------client miss add this transaction------")
                    log.info("------the id is: " + str(tx.txid) + "------")
                    server1 = PeerServer()
                    server1.broadcast_tx(tx)
                    log.info("------client handle_miss broadcast------")
        msg = Msg(Msg.NONE_MSG, "")
        self.send(msg)

    def close(self):
        self.sock.close()


class PeerServer(Singleton):
    def __init__(self):
        if not hasattr(self, "peers"):
            self.peers = []
        if not hasattr(self, "nodes"):
            self.nodes = []
        if not hasattr(self, "ips"):
            self.ips = []
        if not hasattr(self, "longest_chain"):
            self.longest_chain = None

    def get_ip(self, ifname='ens33'):  # enp2s0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(
            fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])

    def nodes_find(self, p2p_server):
        log.info("------------")
        local_ip = self.get_ip()
        while True:
            nodes = p2p_server.get_nodes()
            log.info("-------------")
            for node in nodes:
                if node.ip not in self.ips:
                    log.info("------------nodes_find: " + node.ip + "------------")  # 7.8
                    ip = node.ip
                    port = node.port
                    if local_ip == ip:
                        log.info("------local_ip==ip------")  # 7.8
                        continue
                    log.info("------------nodes ip: " + node.ip + "------------")  # 7.8
                    client = TCPClient(ip, port)
                    log.info("------create TCPClient in nodes_find------")  # 7.8
                    t = threading.Thread(target=client.shake_loop, args=())
                    t.start()
                    log.info("------peer nodes_find: start the thread shake_loop------")
                    self.peers.append(client)
                    self.nodes.append(node)
                    self.ips.append(ip)
            time.sleep(1)

    def broadcast_tx(self, tx):
        log.info("------peerserver broadcast_tx------")  # 7.10
        for peer in self.peers:
            log.info("------peerserver broadcast for------")  # 7.15
            peer.add_tx(tx)
            log.info("------peerserver broadcast add------")  # 7.15

    def run(self, p2p_server):
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
