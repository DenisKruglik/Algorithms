import math
from abs_hash_table import AbstractHashTable


class ChainCollisionHashTable(AbstractHashTable):
    CONST = 797
    A = (math.sqrt(5) - 1) / 2

    def __init__(self, size, koef=A):
        self.data = [[] for i in range(size)]
        self.koef = koef

    def __contains__(self, item):
        ind = self.hash(item)
        for v in self.data[ind]:
            if v == item:
                return True
        return False

    def set(self, value):
        ind = self.hash(value)
        for indd, v in enumerate(self.data[ind]):
            if v == value:
                return
        else:
            self.data[ind].append(value)

    def hash(self, key):
        return math.floor((key % ChainCollisionHashTable.CONST * self.koef) % 1 * len(self.data))

    def longest_chain(self):
        res = 0
        for chain in self.data:
            length = len(chain)
            if length > res:
                res = length
        return res
