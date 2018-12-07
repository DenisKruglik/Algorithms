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
    labels = {v: None for v in range(graph.vertex_count) if v != start}
    current_label = 1
    labels[start] = current_label
    stack = [start]
    visited = [start]
    current_label += 1
    min_converse = {}
    straight = []
    converse = []
    status = True
    joint_point = None

    while len(stack) > 0:
        v = stack[-1]
        label = labels[v]

        for u, e in enumerate(graph.matrix[v]):
            if e is not None and u not in visited:
                stack.append(u)
                labels[u] = current_label
                visited.append(u)
                current_label += 1
                straight.append({v, u})
                if len(list(filter(lambda edge: start in edge, straight))) > 1:
                    status = False
                    joint_point = start if joint_point is None else joint_point
                break
        else:
            for u, e in enumerate(graph.matrix[v]):
                if e is not None and u in visited and {v, u} not in straight and {v, u} not in converse:
                    converse.append({v, u})
                    l = labels[next(filter(lambda i: i == u, stack))]
                    min_converse[v] = l if min_converse.get(v) is None else min(min_converse.get(v), l)

            if label > 1 \
                    and (min_converse.get(v) is None or min_converse.get(v) >= label):
                if len(list(filter(lambda edge: edge is not None, graph.matrix[v]))) > 1\
                        or not graph.has_edge([v, start]):
                    status = False
                    joint_point = v if joint_point is None else joint_point

            if min_converse.get(v) is not None and min_converse[v] < label and len(stack) > 1:
                min_converse[stack[-2]] = min_converse[v]

            stack.pop()

    return status, joint_point, straight, labels
