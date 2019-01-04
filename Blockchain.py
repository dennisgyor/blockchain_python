#!usr/bin/env python3

import hashlib
import json
from time import time
from uuid import uuid4


class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        # self.nodes = set()

        '''Create genesis block. You need the original hash to build the
        rest of the Blockchain.'''
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount

        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        print(self.current_transactions)
        return self.last_block['index'] + 1

    def update_state(self, transaction, state):
        state = state.copy()

        for key in transaction:
            if key in state.keys():
                state[key] += transaction[key]
            else:
                state[key] = transaction[key]

        return state

    def valid_transaction(self, current_transactions, state):
        """A valid transaction must sum to 0."""
        if sum(current_transactions.values()) is not 0:
            return False

        for key in current_transactions.keys():
            if key in state.keys():
                account_balance = state[key]
            else:
                account_balance = 0

            if account_balance + current_transactions[key] < 0:
                return False

        return True
        return self.last_block['index'] + 1

    def resolve_conflicts():
        pass
    '''TODO: need to add conflict resolution | race condition method'''

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: <dict> Block
        :return: <str>
        """

        '''Ensure ordered hashes'''
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
