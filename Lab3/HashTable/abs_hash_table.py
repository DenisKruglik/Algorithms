import math
from abc import ABCMeta, abstractmethod


class AbstractHashTable(metaclass=ABCMeta):

    @abstractmethod
    def set(self, value):
        pass

    @abstractmethod
    def hash(self, value):
        pass
