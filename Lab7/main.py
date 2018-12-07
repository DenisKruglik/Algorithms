import copy
from algorithms import check_duplicity, dfs


def complete_biconnected(graph):
    result = copy.deepcopy(graph)

    while True:
        status, joint_point, straight, d = check_duplicity(result)

        if status:
            return result

        if joint_point == 0:
            to_connect = []
            for e in filter(lambda e: 0 in e, straight):
                to_connect.append((e - {0}).pop())
            for v in range(len(to_connect) - 1):
                result.insert_edge([to_connect[v], to_connect[v+1]])
            if len(to_connect) > 2:
                result.insert_edge([to_connect[0], to_connect[-1]])
            continue

        current = joint_point

        while len(list(filter(lambda e: current in e and d[(e - {current}).pop()] > d[current], straight))) > 0:
            e = next(filter(lambda e: current in e and d[(e - {current}).pop()] > d[current], straight))
            current = (e - {current}).pop()

        result.insert_edge([current, 0])
