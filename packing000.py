# packing function select a list txs = [...]
# until > 1MB or no tx
# verify if tx are valid
# return txs to be used in add_block(transactions)
# wait copy the verify function from other .py
# add info in start in cli.py : # log.info("mined a block")

"""
1. search in txpool : delete invalid transactions
2. sort the txpool
3. start add transactions into the list : until > 1MB or no tx
4. delete the packed transactions from the txpool
4. return the list of transactions (to be used in add_block)
"""

import sys
import threading
from txpool import *
from block_chain import *
from sorting import *


class NotError(Exception):
    pass


def packing():
    bc1 = BlockChain()  # used to verify the transactions
    tx_pool1 = TxPool()
    total_fee = 0   # total fee 6.19
    for tx1 in tx_pool1.txs:    # 1. search in txpool : delete invalid transactions
        if not bc1.verify_transaction(tx1):
            # raise NotError('valid')
            tx_pool1.txs.remove(tx1)
            # raise NotError('invalid')
    tx_pool1.txs = sorting(tx_pool1.txs)    # 2. sort the txpool
    selected_txs = []
    for tx1 in tx_pool1.txs: # 3. start add transactions into the list : until > 1MB or no tx
        selected_txs.append(tx1)
        if sys.getsizeof(selected_txs) > 1048576:
            # raise NotError('bigger than 1 MB') # wait
            selected_txs.remove(tx1)
            break
        else:
            tx_pool1.txs.remove(tx1)    # 4. delete the packed transactions from the txpool
            total_fee += tx1.amount    # add the fee
    return selected_txs, total_fee  # change 6.20

def calculate_total_fee():
    total_fee = 0

def finding_new_block():
    while True:
        bc1 = BlockChain()
        tx3, total_fee = packing()
        bc1.add_block(tx3, total_fee)    # wait try when there's no transaction

def start_find():
    t1 = threading.Thread(target=finding_new_block,args=()) # change
    t1.start()  # change
