# coding:utf-8
from utils import Singleton

class TxPool(Singleton):    # only one in whole node
    SIZE = 0    # change to 0 : will be useless
    def __init__(self):
        if not hasattr(self, "txs"):
            self.txs = []

    def is_full(self):  # change : will be useless
        return len(self.txs) >= self.SIZE   # change : will be useless

    def add(self, tx):
        self.txs.append(tx)

    def clear(self):
        self.txs.clear()
