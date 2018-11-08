from graph.incidence_matrix_graph import IncidenceMatrixGraph


def union(g1, g2):
    if g1.vertex_count != g2.vertex_count:
        raise Exception('Graphs must have equal amount of vertices')

    result = IncidenceMatrixGraph()

    for i in range(g1.vertex_count):
        result.insert_vertex()

    for i in range(g1.vertex_count - 1):
        for j in range(i+1, g1.vertex_count):
            if g1.matrix[i][j] is not None:
                result.insert_edge([i, j], g1.matrix[i][j])
            elif g2.matrix[i][j] is not None:
                result.insert_edge([i, j], g2.matrix[i][j])

    return result
