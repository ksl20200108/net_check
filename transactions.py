# coding:utf-8
import binascii
import ecdsa
import sys  # change
import time     # change
from utils import sum256_hex, hash_public_key, address_to_pubkey_hash

subsidy = 50    # change

class TXOutput(object):
    def __init__(self, value, pub_key_hash=''):
        self.value = value  # how much
        self.pub_key_hash = pub_key_hash

    def lock(self, address):
        hex_pub_key_hash = binascii.hexlify(address_to_pubkey_hash(address))
        self.pub_key_hash = hex_pub_key_hash

    def is_locked_with_key(self, pub_key_hash):
        return self.pub_key_hash == pub_key_hash

    def serialize(self):
        return self.__dict__

    def __repr__(self):
        return 'TXOutput(value={value}, pub_key_hash={pub_key_hash})'.format(
            value=self.value, pub_key_hash=self.pub_key_hash)

    @classmethod
    def deserialize(cls, data):
        value = data.get('value', 0)
        pub_key_hash = data.get('pub_key_hash', 0)
        return cls(value, pub_key_hash)


class TXInput(object):
    def __init__(self, txid, vout, pub_key):
        self.txid = txid
        self.vout = vout  # index of outpus
        self.signature = ''
        self.pub_key = pub_key

    def use_key(self, pub_key_hash):
        bin_pub_key = binascii.unhexlify(self.pub_key)
        hash = hash_public_key(bin_pub_key)
        return pub_key_hash == hash

    def serialize(self):
        return self.__dict__

    def __repr__(self):
        return 'TXInput(txid={txid}, vout={vout})'.format(
            txid=self.txid, vout=self.vout)

    @classmethod
    def deserialize(cls, data):
        txid = data.get('txid', '')
        vout = data.get('vout', 0)
        signature = data.get('signature', '')
        pub_key = data.get('pub_key', '')
        tx_input = cls(txid, vout, pub_key)
        tx_input.signature = signature
        return tx_input


class Transaction(object):
    def __init__(self, vins, vouts, amount=0):
        self.txid = ''
        self.vins = vins
        self.vouts = vouts
        self.generation_time = time.time()      # change
        self.amount = amount   # change 6.19
        self.fee_size_ratio = self.amount / (sys.getsizeof(self.vins) + sys.getsizeof(self.vouts) + sys.getsizeof(self.generation_time) + sys.getsizeof(self.amount))   # change 6.19

    def set_id(self):
        data_list = [str(vin.serialize()) for vin in self.vins]
        vouts_list = [str(vout.serialize()) for vout in self.vouts]
        data_list.extend(vouts_list)
        data = ''.join(data_list)
        hash = sum256_hex(data)
        self.txid = hash

    def is_coinbase(self):
        return len(self.vins) == 1 and len(self.vins[0].txid) == 0 and self.vins[0].vout == -1

    def serialize(self):
        return {
            'txid': self.txid,
            'vins': [vin.serialize() for vin in self.vins],
            'vouts': [vout.serialize() for vout in self.vouts],
            'generation_time': self.generation_time,  # change
            'amount': self.amount,   # change
            'fee_size_ratio': self.fee_size_ratio   # change
        }

    @classmethod
    def deserialize(cls, data):
        txid = data.get('txid', '')
        vins_data = data.get('vins', [])
        vouts_data = data.get('vouts', [])
        generation_time = data.get('generation_time', '')   # change
        amount = data.get('amount', '') # change
        fee_size_ratio = data.get('fee_size_ratio', '') # change
        vins = []
        vouts = []
        for vin_data in vins_data:
            vins.append(TXInput.deserialize(vin_data))

        for vout_data in vouts_data:
            vouts.append(TXOutput.deserialize(vout_data))
        tx = cls(vins, vouts)
        tx.txid = txid
        tx.generation_time = generation_time    # change
        tx.amount = amount  # change
        tx.fee_size_ratio = fee_size_ratio  # change
        return tx

    @classmethod
    def coinbase_tx(cls, to, data, fee=0):   # change add "fee"
        if not data:
            data = "Reward to '%s'" % to
        txin = TXInput('', -1, data)
        txout = TXOutput(subsidy+fee, to)   # change 6.19
        tx = cls([txin], [txout])
        tx.set_id()
        tx.generation_time = time.time()    # change 6.19
        tx.amount = 50 + fee  # change
        tx.fee_size_ratio = (50 + fee) / (sys.getsizeof(tx.vins) + sys.getsizeof(tx.vouts) + sys.getsizeof(tx.generation_time) + sys.getsizeof(tx.amount))  # change
        return tx

    def __repr__(self):
        return 'Transaction(txid={txid}, vins={vins}, vouts={vouts})'.format(
            txid=self.txid, vins=self.vins, vouts=self.vouts)

    def _trimmed_copy(self):
        inputs = []
        outputs = []

        for vin in self.vins:
            inputs.append(TXInput(vin.txid, vin.vout, None))

        for vout in self.vouts:
            outputs.append(TXOutput(vout.value, vout.pub_key_hash))
        tx = Transaction(inputs, outputs)
        tx.txid = self.txid
        return tx

    def sign(self, priv_key, prev_txs):
        if self.is_coinbase():
            return
        tx_copy = self._trimmed_copy()

        for in_id, vin in enumerate(tx_copy.vins):
            prev_tx = prev_txs.get(vin.txid, None)
            if not prev_tx:
                raise ValueError('Previous transaction is error')
            tx_copy.vins[in_id].signature = None
            tx_copy.vins[in_id].pub_key = prev_tx.vouts[vin.vout].pub_key_hash
            tx_copy.set_id()
            tx_copy.vins[in_id].pub_key = None

            sk = ecdsa.SigningKey.from_string(
                binascii.a2b_hex(priv_key), curve=ecdsa.SECP256k1)
            sign = sk.sign(tx_copy.txid.encode())
            self.vins[in_id].signature = binascii.hexlify(sign).decode()

    def verify(self, prev_txs):
        if self.is_coinbase():
            return True
        tx_copy = self._trimmed_copy()

        for in_id, vin in enumerate(self.vins):
            prev_tx = prev_txs.get(vin.txid, None)
            if not prev_tx:
                raise ValueError('Previous transaction is error')
            tx_copy.vins[in_id].signature = None
            tx_copy.vins[in_id].pub_key = prev_tx.vouts[vin.vout].pub_key_hash
            tx_copy.set_id()
            tx_copy.vins[in_id].pub_key = None

            sign = binascii.unhexlify(self.vins[in_id].signature)
            vk = ecdsa.VerifyingKey.from_string(
                binascii.a2b_hex(vin.pub_key), curve=ecdsa.SECP256k1)
            if not vk.verify(sign, tx_copy.txid.encode()):
                return False

        end_time = time.time()  # change
        if (end_time - self.generation_time) > 1200 : # 1200:    # change
            return False    # change
        return True

    # def calculate_fee_size_ratio(self, fee): # change
    #     return fee / (sys.getsizeof(self.vins) + sys.getsizeof(self.vouts) + sys.getsizeof(self.generation_time) + sys.getsizeof(self.amount))
