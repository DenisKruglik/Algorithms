from graph.abstract_graph import AbstractGraph


class IncidenceMatrixGraph(AbstractGraph):
    def __init__(self):
        self.matrix = []
        self.vertex_count = 0

    def insert_vertex(self):
        self.vertex_count += 1

        for row in self.matrix:
            row.append(None)

        self.matrix.append([None] * self.vertex_count)

    def insert_edge(self, edge, weight):
        v1, v2 = edge
        if self.has_vertex(v1) and self.has_vertex(v2):
            self.matrix[v1][v2] = weight
            self.matrix[v2][v1] = weight
        else:
            raise Exception('Vertices of the edge must be contained in the graph')

    def vertices_adjacent(self, v1, v2):
        if self.has_vertex(v1) and self.has_vertex(v2):
            return self.matrix[v1][v2] is not None
        else:
            raise Exception('Vertices must be contained in the graph')

    def edges_adjacent(self, e1, e2):
        if self.has_edge(e1) and self.has_edge(e2):
            return len(set(e1) & set(e2)) > 0
        else:
            raise Exception('Edges must be contained in the graph')

    def remove_vertex(self, vertex):
        if self.has_vertex(vertex):
            self.vertex_count -= 1
            del self.matrix[vertex]

            for row in self.matrix:
                del row[vertex]

        else:
            raise Exception('Vertex must be contained in the graph')

    def remove_edge(self, edge):
        if self.has_edge(edge):
            v1, v2 = edge
            self.matrix[v1][v2] = None
            self.matrix[v2][v1] = None
        else:
            raise Exception('Edge must be contained in the graph')

    def get_neighbourhood(self, vertex):
        result = []

        for i, v in enumerate(self.matrix[vertex]):
            if v is not None:
                result.append(i)

        return result

    def has_vertex(self, v):
        return 0 <= v < self.vertex_count

    def has_edge(self, edge):
        return self.vertices_adjacent(*edge)

    def clear(self):
        self.matrix.clear()
        self.vertex_count = 0

    def is_connected(self):
        if self.vertex_count < 2:
            return True

        not_to_check = []

        for rind, row in enumerate(self.matrix):
            if rind not in not_to_check:
                for vind, v in enumerate(row):
                    if v is not None:
                        if vind not in not_to_check:
                            not_to_check.append(vind)
                        break
                else:
                    break
        else:
            return True

        return False
