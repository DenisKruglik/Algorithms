from graph.incidence_matrix_graph import IncidenceMatrixGraph


'''Module contains algorithms for lab.'''


def prim(graph):
    '''Prim's algorithm

    Args:
        graph (IncidenceMatrixGraph): graph to apply algorithm to

    Returns:
        IncidenceMatrixGraph: minimum weight spanning tree'''

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


def kruskal(graph):
    '''Kruskal's algorithm

    Args:
        graph (IncidenceMatrixGraph): graph to apply algorithm to

    Returns:
        IncidenceMatrixGraph: minimum weight spanning tree'''

    if not graph.is_connected():
        raise Exception('Graph must be connected')

    if graph.vertex_count < 3:
        return graph

    edges = []

    for i in range(graph.vertex_count - 1):
        for j in range(i+1, graph.vertex_count):
            if graph.matrix[i][j] is not None:
                edges.append(((i, j), graph.matrix[i][j]))

    edges.sort(key=lambda edge: edge[1])

    result = IncidenceMatrixGraph()

    for i in range(graph.vertex_count):
        result.insert_vertex()

    component_map = {i: i for i in range(graph.vertex_count)}

    for e in edges:
        v1, v2 = e[0]
        if component_map[v1] != component_map[v2]:
            result.insert_edge(*e)
            new = min(component_map[v1], component_map[v2])
            old = component_map[v1] if new == component_map[v2] else component_map[v2]

            for k in component_map:
                if component_map[k] == old:
                    component_map[k] = new

            if len(set(component_map.values())) == 1:
                break

    return result


def gale_shapley(men, women):
    '''Gale-Shapley algorithm

    Args:
        men (list): matrix of men's women preferences represented as list of lists, each row for each man contains indices of women ordered by preference
        women (list): same matrix for women

    Returns:
        list: result distribution represented by list where index is an index of a man and value is an index of a woman assigned

    Example:
        men = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 3, 1]
        ]

        women = [
            [2, 3, 1],
            [1, 3, 2],
            [2, 1, 3]
        ]

        gale_shapley(men, women)'''

    blacklists = [[]] * len(men)

    marriage_map = [None for i in range(len(men))]

    while len({i for i, v in enumerate(marriage_map) if v is None}) > 0:
        man = next(filter(lambda i: i[1] is None, enumerate(marriage_map)))[0]

        for w in men[man]:
            if w not in blacklists[man]:
                current_man = marriage_map.index(w) if w in marriage_map else None

                if current_man is None:
                    marriage_map[man] = w
                    break

                if women[w].index(man) < women[w].index(current_man):
                    marriage_map[man] = w
                    marriage_map[current_man] = None
                    blacklists[current_man].append(w)
                    break
                else:
                    blacklists[man].append(w)

    return marriage_map
