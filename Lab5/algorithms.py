from graph.incidence_matrix_graph import IncidenceMatrixGraph


def prim(graph):
    if not graph.is_connected():
        raise Exception('Graph must be connected')

    if graph.vertex_count < 3:
        return graph

    result = IncidenceMatrixGraph()

    for i in range(graph.vertex_count):
        result.insert_vertex()

    control_component = {0}

    while len(control_component) != graph.vertex_count:
        min_edge = None

        for i in control_component:
            for j, val in enumerate(graph.matrix[i]):
                if j not in control_component and val is not None and (min_edge is None or val < graph.matrix[min_edge[0]][min_edge[1]]):
                    min_edge = [i, j]

        result.insert_edge(min_edge, graph.matrix[min_edge[0]][min_edge[1]])
        control_component.add(min_edge[1])

    return result
