#!usr/bin/env python3

from Blockchain import Blockchain as b
'''Test the creation of a new Blockchain'''
x = b()
y = x.new_block(2)

print(y)

'''Add a new transaction to the blockchain'''
d = b()
a = d.new_transaction('9000', '9010', 6)

print(a)

c = b()
e = c.new_transaction('9001', '9010', 1)

print(e)
