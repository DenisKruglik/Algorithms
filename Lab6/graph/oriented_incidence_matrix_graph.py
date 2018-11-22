from graph.incidence_matrix_graph import IncidenceMatrixGraph


class OrientedIncidenceMatrixGraph(IncidenceMatrixGraph):
    def insert_edge(self, edge, weight):
        '''Add an edge between specified vertices

        Args:
            edge (list): list of 2 vertex indices to connect
            weight (int): Weight of the edge added

        Raises:
            Exception: edge contains indices of vertices not present in the graph

        Example:
            graph.insert_edge([0, 3], 5) - connects vertices 0 and 3 with an edge of weight 5'''

        v1, v2 = edge
        if self.has_vertex(v1) and self.has_vertex(v2):
            self.matrix[v1][v2] = weight
        else:
            raise Exception('Vertices of the edge must be contained in the graph')

    def remove_edge(self, edge):
        '''Removes edge from the graph

        Args:
            edge (list): list of two vertices on the ends of the edge

        Raises:
            Exception: edge contains indices of vertices not present in the graph

        Example:
            graph.remove_edge([0, 3])'''

        if self.has_edge(edge):
            v1, v2 = edge
            self.matrix[v1][v2] = None
        else:
            raise Exception('Edge must be contained in the graph')