import copy


def euler_cycle_search(graph):
    for v in graph.adjacency_lists:
        if len(graph.adjacency_lists[v]) % 2 != 0:
            return None

    g = copy.deepcopy(graph)
    s = []
    q = []
    s.append(list(g.adjacency_lists.keys())[0])

    while len(s) > 0:
        u = s[-1]
        if len(g.adjacency_lists[u]) > 0:
            removed = g.adjacency_lists[u].pop()
            g.adjacency_lists[removed].remove(u)
            s.append(removed)
        else:
            q.insert(0, s.pop())

    return q
