import copy
from math import inf


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


def dijkstra(graph, begin):
    '''Returns a tuple with the distance dictionary and path dictionary.
    The first one determines min distance to this vertex from the beginning and the second determines from which
    vertex one should come to this one

    Args:
        graph (IncidenceMatrixGraph|OrientedIncidenceMatrixGraph): graph under consideration
        begin (int): index of the beginning vertex

    Returns:
        tuple: tuple of dictionaries of distance and path'''
    dist = {}
    used = {}
    path = {}

    for i in range(graph.vertex_count):
        dist[i] = inf
        used[i] = False

    dist[begin] = 0

    for i in range(graph.vertex_count):
        v = None

        for j in range(graph.vertex_count):
            if not used[j] and (v is None or dist[j] < dist[v]):
                v = j

        if dist[v] == inf:
            break

        used[v] = True

        for u, w in enumerate(graph.matrix[v]):
            if w is not None and dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                path[u] = v
    return dist, path
