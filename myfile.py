title = "The Meaning of Life"
a = 'dead'
b = 'parrot'
c = 'sketch'
print(title)
print(a,b,c)

import decimal, fractions
from collections import namedtuple


Numbers = 1234, 3.1415, 3+4j, 0b111 #, decimal(5, -10), fractions(5, -10)
Strings = 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
Lists = [1, [2, 'three'], 4.5], list(range(10))
Dictionaries = {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
Tuples = (1, 'spam', 4, 'U'), tuple('spam'), namedtuple("Point", "x y")
# Files = open('eggs.txt'), open(r'C:\ham.bin', 'wb')
Sets = set('abc'), {'a', 'b', 'c'}

print('Numbers: ', Numbers)
print('Strings: ', Strings)
print('Lists: ', Lists)
print('Dictionaries: ', Dictionaries)
print('Tuples: ', Tuples)
# print('Files', Files)
print('Sets: ', Sets)