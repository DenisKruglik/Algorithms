import copy


def floyd(graph):
    '''Returns a matrix which determines the shortest distance from any vertex in graph to any other

    Args:
        graph (IncidenceMatrixGraph|OrientedIncidenceMatrixGraph): graph under consideration

    Returns:
        list: list of lists representing a matrix which determines the shortest distance from any vertex in graph to any other'''
    a = copy.deepcopy(graph.matrix)

    for i in range(graph.vertex_count):
        unignored_rows = list(range(graph.vertex_count))
        unignored_rows.remove(i)
        unignored_columns = copy.copy(unignored_rows)

        for j, el in enumerate(a[i]):
            if j != i and el is None:
                unignored_columns.remove(j)

        for j, el in enumerate(a):
            if j != i and el[i] is None:
                unignored_rows.remove(j)

        for row in unignored_rows:
            for col in unignored_columns:
                a[row][col] = min(a[row][col], a[i][col] + a[row][i]) if a[row][col] is not None else a[i][col] + a[row][i]

    return a
