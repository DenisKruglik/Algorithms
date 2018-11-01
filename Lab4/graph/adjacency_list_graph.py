from graph.abstract_graph import AbstractGraph


class AdjacencyListGraph(AbstractGraph):
    def __init__(self):
        self.adjacency_lists = {}

    def insert_vertex(self, vertex, adjacent_vertices=()):
        vertices_correct = True

        for v in adjacent_vertices:
            if v not in self.adjacency_lists:
                self.adjacency_lists[v] = [vertex]
            elif vertex not in self.adjacency_lists[v]:
                self.adjacency_lists[v].append(vertex)

        self.adjacency_lists[vertex] = list(adjacent_vertices)

    def insert_edge(self, edge):
        for v in edge:
            if v not in self.adjacency_lists:
                self.insert_vertex(v)

        if edge[0] not in self.adjacency_lists[edge[1]]:
            self.adjacency_lists[edge[1]].append(edge[0])
            self.adjacency_lists[edge[0]].append(edge[1])

    def vertices_adjacent(self, v1, v2):
        return self.has_edge([v1, v2])

    def edges_adjacent(self, e1, e2):
        if not self.has_edge(e1) or not self.has_edge(e2):
            return False

        return len(set(e1) & set(e2)) > 0

    def remove_vertex(self, vertex):
        for v in self.adjacency_lists[vertex]:
            self.adjacency_lists[v].remove(vertex)

        del self.adjacency_lists[vertex]

    def remove_edge(self, edge):
        self.adjacency_lists[edge[0]].remove(edge[1])
        self.adjacency_lists[edge[1]].remove(edge[0])

    def get_neighbourhood(self, vertex):
        return self.adjacency_lists[vertex]

    def has_vertex(self, v):
        return v in self.adjacency_lists

    def has_edge(self, edge):
        return edge[0] in self.adjacency_lists[edge[1]]

    def clear(self):
        self.adjacency_lists = {}
