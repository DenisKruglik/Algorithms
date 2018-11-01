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


def breadth_first_search(graph, start=None, need_bipartite=False):
    if len(graph.adjacency_lists) == 0:
        return None

    if start is not None and start not in graph.adjacency_lists:
        raise Exception("Starting vertex is not present in a graph")

    g = copy.deepcopy(graph)
    marked = {}

    current_generation = previous_generation = 0
    marked[list(g.adjacency_lists.keys())[0] if start is None else start] = current_generation
    is_bipartite = True

    while True:
        current_generation += 1
        is_end = True

        for i in [k for k in marked if marked[k] == previous_generation]:
            for j in g.adjacency_lists[i]:
                if j not in marked:
                    marked[j] = current_generation
                    is_end = False
                elif need_bipartite and is_bipartite and marked[j] % 2 == marked[i] % 2:
                    is_bipartite = False

        if is_end: break

        previous_generation = current_generation

    return marked if not need_bipartite else (marked, is_bipartite)
