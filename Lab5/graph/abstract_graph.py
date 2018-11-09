from abc import ABCMeta, abstractmethod


class AbstractGraph(metaclass=ABCMeta):
    @abstractmethod
    def insert_vertex(self):
        pass

    @abstractmethod
    def insert_vertices(self, amount):
        pass

    @abstractmethod
    def insert_edge(self, edge, weight):
        pass

    @abstractmethod
    def vertices_adjacent(self, v1, v2):
        pass

    @abstractmethod
    def edges_adjacent(self, e1, e2):
        pass

    @abstractmethod
    def remove_vertex(self, vertex):
        pass

    @abstractmethod
    def remove_edge(self, edge):
        pass

    @abstractmethod
    def get_neighbourhood(self, vertex):
        pass

    @abstractmethod
    def has_vertex(self, v):
        pass

    @abstractmethod
    def has_edge(self, edge):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass
