import math
from abs_hash_table import AbstractHashTable


class ChainCollisionHashTable(AbstractHashTable):
    CONST = 797
    A = (math.sqrt(5) - 1) / 2

    def __init__(self, size, koef=A):
        self.data = [[] for i in range(size)]
        self.koef = koef

    def get(self, key):
        ind = self.hash(key)
        for (k, v) in self.data[ind]:
            if k == key:
                return v
        return None

    def set(self, key, value):
        ind = self.hash(key)
        for indd, (k, v) in enumerate(self.data[ind]):
            if k == key:
                self.data[ind][indd][1] = value
                break
        else:
            self.data[ind].append([key, value])

    def hash(self, key):
        return math.floor((key % ChainCollisionHashTable.CONST * self.koef) % 1 * len(self.data))

    def longest_chain(self):
        res = 0
        for chain in self.data:
            length = len(chain)
            if length > res:
                res = length
        return res
