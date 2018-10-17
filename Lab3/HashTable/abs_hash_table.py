import math
from abc import ABCMeta, abstractmethod


class AbstractHashTable(metaclass=ABCMeta):

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def hash(self, value):
        pass
