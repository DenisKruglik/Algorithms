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

    def __contains__(self, key):
        hashh = self.hash(key)
        ind = hashh
        trry = 0
        while self.data[ind] is not None and self.data[ind] != key:
            trry += 1
            ind = (hashh + (trry ** 2)) % len(self.data)
        return False if self.data[ind] is None else True

    def set(self, value):
        if self._size == self._max_size:
            for val in self.data:
                if val is not None and val == value:
                    return 0
            else:
                raise Exception('Cannot insert new element into a full hash table')

        hashh = self.hash(value)
        ind = hashh
        trry = 0
        while self.data[ind] is not None:
            if self.data[ind] == value:
                return trry
            else:
                trry += 1
                ind = (hashh + (trry ** 2)) % len(self.data)
        self.data[ind] = value
        self._size += 1
        return trry

    def hash(self, key):
        return math.floor(key * OpenAddressingHashTable.PRIME) % len(self.data)