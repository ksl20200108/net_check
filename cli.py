# coding:utf-8
import argparse
import threading
from block_chain import *
from wallet import Wallet
from wallets import Wallets
from utxo import UTXOSet
from txpool import TxPool
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
from network import P2p, PeerServer, TCPServer
from rpcserver import RPCServer
from packing import *   # change
from transactions import *
import couchdb
import random
import pdb  # 7.11
# import sys # change
# from sorting import *   # change

def new_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(help='commands')
    # A print command
    print_parser = sub_parser.add_parser(
        'print', help='Print all the blocks of the blockchain')
    print_parser.add_argument(type=int, dest='height', help='HEIGHT')
    balance_parser = sub_parser.add_parser(
        'balance', help='Print balance of address')
    balance_parser.add_argument(type=str, dest='address', help='ADDRESS')

    send_parser = sub_parser.add_parser(
        'send', help='Send AMOUNT of coins from FROM address to TO')
    send_parser.add_argument(
        '--from', type=str, dest='send_from', help='FROM')
    send_parser.add_argument(
        '--to', type=str, dest='send_to', help='TO')
    send_parser.add_argument(
        '--amount', type=int, dest='send_amount', help='AMOUNT')
    # send_parser.add_argument(   # change
    #     '--fee', type=float, dest='send_fee', help='FEE')   # change

    bc_parser = sub_parser.add_parser(
        'createwallet', help='Create a wallet')
    bc_parser.add_argument('--createwallet', dest='createwallet', help='create wallet')

    prin_wallet_parser = sub_parser.add_parser(
        'printwallet', help='print all wallet')
    prin_wallet_parser.add_argument('--printwallet', dest='printwallet', help='print wallets')

    start_parser = sub_parser.add_parser(
        'start', help='start server')
    start_parser.add_argument('--start', dest='start', help='start server')

    genesis_block_parser = sub_parser.add_parser(
        'genesis_block', help='create genesis block')
    genesis_block_parser.add_argument('--genesis_block', dest='genesis_block')

    start_mining_parser = sub_parser.add_parser('start_mining', help='start find')  # change
    start_mining_parser.add_argument('--start_mining', dest='start_mining') # change

    print_txpool_parser = sub_parser.add_parser('print_txpool', help='print txpool')    # change
    print_txpool_parser.add_argument('--print_txpool', dest='print_txpool') # change

    sort_txpool_parser = sub_parser.add_parser('sort_txpool', help='sort_txpool')  # change
    sort_txpool_parser.add_argument('--sort_txpool', dest='sort_txpool')  # change

    alive_parser = sub_parser.add_parser('alive', help='alive') # 7.18
    alive_parser.add_argument('--alive', dest='alive')  # 7.18

    return parser

class Cli(object):
    def get_balance(self, addr):
        bc = BlockChain()
        balance = 0
        utxo = UTXOSet()
        utxo.reindex(bc)
        utxos = utxo.find_utxo(addr)
        print(utxos)
        for fout in utxos:
            balance += fout.txoutput.value
        print('%s balance is %d' %(addr, balance))
        return balance

    def create_wallet(self):
        w = Wallet.generate_wallet()
        ws = Wallets()
        ws[w.address] = w
        ws.save()
        return w.address

    def print_all_wallet(self):
        ws = Wallets()
        wallets = []
        for k, _ in ws.items():
            wallets.append(k)
        return wallets

    def send(self, from_addr, to_addr, amount):    # change
        bc = BlockChain()
        fee = random.uniform(0.1, 0.6)
        tx = bc.new_transaction(from_addr, to_addr, amount, fee)    # change
        tx_pool = TxPool()
        tx_pool.add(tx)
        try:
            server = PeerServer()   # broadcast to peers
            server.broadcast_tx(tx) # broadcast to peers
            # if tx_pool.is_full():   # change
                # bc.add_block(tx_pool.txs)   # change
                # tx_pool.clear() # change
        except Exception as e:
            pass
        # print('send %d from %s to %s' %(amount, from_addr, to_addr))  # 7.12

    def print_chain(self, height):
        bc = BlockChain()
        return bc[height].block_header.serialize()

    def create_genesis_block(self):
        bc = BlockChain()
        w = Wallet.generate_wallet()
        ws = Wallets()
        ws[w.address] = w
        ws.save()
        tx = bc.coin_base_tx(w.address)
        bc.new_genesis_block(tx)
        return w.address

    def print_txpool(self): # change no problem
        tx_pool1 = TxPool() # change
        return tx_pool1.txs # change

    def start_find(self):   # may be write in one function?
        t1 = threading.Thread(target=finding_new_block, args=()) # change
        t1.start()  # change

    def sort_txpool(self):
        # tx_pool5 = TxPool()
        # txs5 = sorting(tx_pool5.txs)
        # return txs5
        return packing()


def start():    # wait : thread add_block(txs)   txs = []   packing function >1MB or no tx verify if tx are valid
    couch = couchdb.Server("http://127.0.0.1:5984")
    try:
        couch.delete('block_chain')
    except:
        pass
    db = couch.create('block_chain')
    # doc1 = {
    #     "index": 0,
    #     "value": 50,
    #     "pub_key_hash": "1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W"
    # }
    # db.create(doc1)
    # doc2 = {
    #     "_id": "UTXOl",
    #     "height": 0
    # }
    # db.create(doc2)
    # doc3 = {
    #     "_id": "fa2db3113d4598834fcc43719ce613862606588f08ab2d62528ad1204f65a693",
    #     "block_header": {
    #         "height": 0,
    #         "timestamp": "1595317443.8917115",
    #         "nonce": "",
    #         "hash": "fa2db3113d4598834fcc43719ce613862606588f08ab2d62528ad1204f65a693",
    #         "prev_block_hash": "",
    #         "hash_merkle_root": "0b3b993e4e22ffe31624c73c009797f0e7fde2b136d0f4c621bf04382d9e08b2"
    #     },
    #     "magic_no": 3166485692,
    #     "transactions": [
    #         {
    #             "txid": "765864a253859a921dc3a8b8d0cc15c6953c9db9d7fb9bf2119bf7c524073fed",
    #             "generation_time": 1595317443.8886538,
    #             "fee_size_ratio": 0.25510204081632654,
    #             "amount": 50,
    #             "vins": [
    #                 {
    #                     "txid": "",
    #                     "pub_key": "1595317443.8886075",
    #                     "signature": "",
    #                     "vout": -1
    #                     }
    #                 ],
    #             "vouts": [
    #                 {
    #                     "value": 50,
    #                     "pub_key_hash": "1EiVGWYsWiM7shgR5i9KTE2kUjzqcyQU9W"
    #                     }
    #                 ]
    #         }
    #     ]
    # }
    # db.create(doc3)
    # doc4 = {
    #     "_id": "l",
    #     "hash": "fa2db3113d4598834fcc43719ce613862606588f08ab2d62528ad1204f65a693"
    # }
    # db.create(doc4)
    # print("initialize database successfully")

    bc = BlockChain()   # only one blockchain called bc
    utxo_set = UTXOSet()
    utxo_set.reindex(bc)

    tcpserver = TCPServer()
    tcpserver.listen()
    tcpserver.run()

    rpc = RPCServer(export_instance=Cli())
    rpc.start(False)

    p2p = P2p()
    server = PeerServer()
    server.run(p2p)
    p2p.run()


def main():
    parser = new_parser()
    args = parser.parse_args()

    s = ServerProxy("http://localhost:9999")
    if hasattr(args, 'height'):
        block_data = s.print_chain(args.height)
        print(block_data)

    if hasattr(args, 'address'):
        balance = s.get_balance(args.address)
        print("%s balance is %d" %(args.address, balance))

    if hasattr(args, 'createwallet'):
        address = s.create_wallet()
        print('Wallet address is %s' % address)

    if hasattr(args, 'start'):
        start()

    if hasattr(args, 'printwallet'):
        wallets = s.print_all_wallet()
        print('Wallet are:')
        for wallet in wallets:
            print("\t%s" % wallet)

    if hasattr(args, 'genesis_block'):
        address = s.create_genesis_block()
        print('Genesis Wallet is: %s' % address)

    if hasattr(args, 'send_from') \
        and hasattr(args, 'send_to') \
        and hasattr(args, 'send_amount')\
        and hasattr(args, 'send_fee'):  # change
        s.send(args.send_from, args.send_to, args.send_amount, args.send_fee)   # change

    if hasattr(args, 'start_mining'):    # change
        print("start mining...")    # change
        s.start_find()    # change
        print("after start_find")   # 7.10

    if hasattr(args, 'print_txpool'):   # change
        txs = s.print_txpool()    # change
        print(type(txs[0])) # dict
        for tx in txs:  # change
            print("transaction: ", tx)  # change

    if hasattr(args, 'sort_txpool'):
        txs6, no = s.sort_txpool()
        # for i in range(len(txs6)):
        #     txs6[i] = Transaction.deserialize(txs6[i])
        #     print("transaction: ", type(txs6[i]))
        utxo_set = UTXOSet()
        txs6 = utxo_set.clear_transactions(txs6)
        print(txs6)

    if hasattr(args, 'alive'):
        chain_doc = []
        bc1 = BlockChain()
        last_blo = bc1.get_last_block()
        last_height = last_blo.block_header.height
        for i in range(0, last_height+1):
            blo = bc1.get_block_by_height(i)
            print(blo.serialize())
            print("")


if __name__ == "__main__":
    main()
