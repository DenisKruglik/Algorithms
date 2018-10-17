import math
from abs_hash_table import AbstractHashTable


class OpenAddressingHashTable(AbstractHashTable):
    PRIME = 1933

    def __init__(self, size):
        self._size = 0
        self._max_size = size
        data_len = 0
        while size > 0:
            size >>= 1
            data_len += 1
        self.data = [None] * (2**data_len)

    def get(self, key):
        hashh = self.hash(key)
        ind = hashh
        trry = 0
        while self.data[ind] is not None and self.data[ind][0] != key:
            trry += 1
            ind = (hashh + (trry ** 2)) % len(self.data)
        return None if self.data[ind] is None else self.data[ind][1]

    def set(self, key, value):
        if self._size == self._max_size:
            for index, val in enumerate(self.data):
                if val is not None and val[0] == key:
                    self.data[index][1] = value
                    break
            else:
                raise Exception('Cannot insert new element into a full hash table')

        hashh = self.hash(key)
        ind = hashh
        trry = 0
        while self.data[ind] is not None:
            if self.data[ind][0] != key:
                trry += 1
                ind = (hashh + (trry ** 2)) % len(self.data)
            else:
                self.data[ind][1] = value
                return trry
        self.data[ind] = [key, value]
        self._size += 1
        return trry

    def hash(self, key):
        return math.floor(key * OpenAddressingHashTable.PRIME) % len(self.data)