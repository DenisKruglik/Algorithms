from graph.abstract_graph import AbstractGraph


class IncidenceMatrixGraph(AbstractGraph):
    '''Graph implementation based on incidence matrix, vertices are represented by the index of their row in a matrix.
    Graph contains matrix and a vertex amount counter.'''

    def __init__(self):
        self.matrix = []
        self.vertex_count = 0

    def insert_vertex(self):
        '''Adds a single vertex to the graph'''

        self.vertex_count += 1

        for row in self.matrix:
            row.append(None)

        self.matrix.append([None] * self.vertex_count)

    def insert_vertices(self, amount):
        '''Adds multiple single vertices to the graph

        Args:
            amount (int): Amount of vertices added'''

        for i in range(amount):
            self.insert_vertex()

    def insert_edge(self, edge, weight=1):
        '''Add an edge between specified vertices

        Args:
            edge (list|tuple): list of 2 vertex indices to connect
            weight (int): Weight of the edge added

        Raises:
            Exception: edge contains indices of vertices not present in the graph

        Example:
            graph.insert_edge([0, 3], 5) - connects vertices 0 and 3 with an edge of weight 5'''

        v1, v2 = edge
        if self.has_vertex(v1) and self.has_vertex(v2):
            self.matrix[v1][v2] = weight
            self.matrix[v2][v1] = weight
        else:
            raise Exception('Vertices of the edge must be contained in the graph')

    def vertices_adjacent(self, v1, v2):
        '''Checks if two vertices are adjacent

        Args:
            v1 (int): index of the first vertex
            v2 (int): index of the second vertex

        Returns:
            bool: True if vertices are adjacent, False otherwise

        Raises:
            Exception: some of vertices not present in the graph

        Example:
            graph.vertices_adjacent(0, 3)'''

        if self.has_vertex(v1) and self.has_vertex(v2):
            return self.matrix[v1][v2] is not None
        else:
            raise Exception('Vertices must be contained in the graph')

    def edges_adjacent(self, e1, e2):
        '''Checks if two edges are adjacent

        Args:
            e1 (list|tuple): list of two vertices on the ends of the first edge
            e2 (list|tuple): list of two vertices on the ends of the second edge

        Returns:
            bool: True if edges are adjacent, False otherwise

        Raises:
            Exception: edges contain indices of vertices not present in the graph

        Example:
            graph.vertices_adjacent([0, 3], [3, 2])'''

        if self.has_edge(e1) and self.has_edge(e2):
            return len(set(e1) & set(e2)) > 0
        else:
            raise Exception('Edges must be contained in the graph')

    def remove_vertex(self, vertex):
        '''Removes vertex from the graph

        Args:
            vertex (int): index of a vertex removed

        Raises:
            Exception: vertex is not present in the graph

        Example:
            graph.remove_vertex(3)'''

        if self.has_vertex(vertex):
            self.vertex_count -= 1
            del self.matrix[vertex]

            for row in self.matrix:
                del row[vertex]

        else:
            raise Exception('Vertex must be contained in the graph')

    def remove_edge(self, edge):
        '''Removes edge from the graph

        Args:
            edge (list|tuple): list of two vertices on the ends of the edge

        Raises:
            Exception: edge contains indices of vertices not present in the graph

        Example:
            graph.remove_edge([0, 3])'''

        if self.has_edge(edge):
            v1, v2 = edge
            self.matrix[v1][v2] = None
            self.matrix[v2][v1] = None
        else:
            raise Exception('Edge must be contained in the graph')

    def get_neighbourhood(self, vertex):
        '''Returns list of vertices that are adjacent with the considered

        Args:
            vertex (int): index of a vertex

        Returns:
            list: list of vertices that are adjacent with the considered'''

        result = []

        for i, v in enumerate(self.matrix[vertex]):
            if v is not None:
                result.append(i)

        return result

    def has_vertex(self, v):
        '''Checks if vertex with such index is contained in the graph

        Args:
            v (int): index of a vertex

        Returns:
            bool: True if vertex is present in the graph, False otherwise'''

        return 0 <= v < self.vertex_count

    def has_edge(self, edge):
        '''Checks if edge is contained in the graph

        Args:
            edge (list|tuple): list of two vertices on the ends of the edge

        Returns:
            bool: True if edge is present in the graph, False otherwise

        Example:
            graph.has_edge([0, 3])'''

        return self.vertices_adjacent(*edge)

    def clear(self):
        '''Removes all the vertices from the graph'''

        self.matrix.clear()
        self.vertex_count = 0

    def is_connected(self):
        '''Checks if graph is connected

        Returns:
            bool: True if graph is connected, False otherwise'''

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
