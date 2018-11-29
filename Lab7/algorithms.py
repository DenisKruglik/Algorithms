def dfs(graph, start):
    '''Depth-first search

        Args:
            graph (IncidenceMatrixGraph): graph considered
            start (int): index of a vertex to begin search from

        Returns:
            tuple: tuple contains a list of straight arcs, a list of converse arcs and a dictionary of labels'''
    d = {v: None for v in range(graph.vertex_count) if v != start}
    k = 1
    d[start] = k
    q = [start]
    straight = []
    converse = []

    while len(q) > 0:
        v = q[-1]

        for u, e in enumerate(graph.matrix[v]):
            if e is not None:
                if d[u] is None:
                    straight.append({u, v})
                    k += 1
                    d[u] = k
                    q.append(u)
                    break
                elif {u, v} not in straight and {u, v} not in converse:
                    converse.append({u, v})
        else:
            q.pop()

    return straight, converse, d
