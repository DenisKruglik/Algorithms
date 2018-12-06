def dfs(graph, start=0):
    '''Depth-first search

        Args:
            graph (IncidenceMatrixGraph): graph considered
            start (int): index of a vertex to begin search from

        Returns:
            tuple: tuple contains a list of straight arcs, a list of converse arcs and a dictionary of labels'''
    d = {v: None for v in range(graph.vertex_count) if v != start}
    k = 0
    d[k] = k
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


def check_duplicity(graph, start=0):
    current_label = 1
    stack = [(start, current_label)]
    visited = [start]
    current_label += 1
    min_converse = None
    straight = []
    converse = []

    while len(stack) > 0:
        v, label = stack[-1]

        for u, e in enumerate(graph.matrix[v]):
            if e is not None and u not in visited:
                stack.append((u, current_label))
                visited.append(u)
                current_label += 1
                straight.append({v, u})
                if len(list(filter(lambda edge: start in edge, straight))) > 1:
                    return False
                break
        else:
            for u, e in enumerate(graph.matrix[v]):
                if e is not None and u in visited and {v, u} not in straight and {v, u} not in converse:
                    converse.append({v, u})
                    l = next(filter(lambda i: i[0] == u, stack))[1]
                    min_converse = l if min_converse is None else min(min_converse, l)

            if label > 1 and (min_converse is None or min_converse >= label):
                return False

            stack.pop()

    return True
