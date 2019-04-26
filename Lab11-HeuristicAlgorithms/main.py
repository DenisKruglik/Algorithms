from sortings import hybrid_sort as hsort
import re
from fractions import Fraction
from math import inf
from graph.incidence_matrix_graph import IncidenceMatrixGraph as Graph


NUMBER_REGEXP = re.compile('^\d+(\.(\d)*)?$')
FRACTION_REGEXP = re.compile('^\d+/\d+$')


def first_fit_sorting(items):
    containers = [[]]
    items = hsort(items, 10)
    for i in items:
        if i > 1: continue
        for c in containers:
            if sum(c) + i <= 1:
                c.append(i)
                break
        else:
            containers.append([i])
    return containers


def first_fit_dynamic():
    containers = [[]]

    def add_item():
        num = input('Enter item weight: ')
        while True:
            if NUMBER_REGEXP.match(num):
                num = float(num)
                break
            elif FRACTION_REGEXP.match(num):
                num = Fraction(num)
                break
            else:
                continue
        if num > 1:
            print('Weight mustn\'t be greater than 1')
            return
        for c in containers:
            if sum(c) + num <= 1:
                c.append(num)
                break
        else:
            containers.append([num])

    def print_containers():
        for c in containers:
            print(c, sum(c))

    while True:
        command = input('Choose action:\n1. Add item\n2. Print containers').strip()
        action = {'1': add_item, '2': print_containers}.get(command, None)
        if action:
            action()
        else:
            print('Invalid input')


def hamiltonian_cycle(graph):
    for i in range(graph.vertex_count):
        for j in range(i+1, graph.vertex_count):
            if graph.matrix[i][j] is None:
                graph.insert_edge((i, j), inf)

    edges = [(i, i+1) for i in range(graph.vertex_count-1)] + [(graph.vertex_count-1, 0)]
    def weight(edge): return graph.matrix[edge[0]][edge[1]]
    edges.sort(key=weight, reverse=True)
    result = Graph()
    result.insert_vertices(graph.vertex_count)
    for e in edges:
        result.insert_edge(e, graph.matrix[e[0]][e[1]])
    def sum_weight(edgs): return sum(map(weight, edgs))
    highscore = edges
    def graph_to_edges(g):
        return [(i, j) for i in range(g.vertex_count) for j in range(i+1, g.vertex_count) if g.matrix[i][j] is not None]
    blacklist = []
    for i, e1 in enumerate(edges):
        for j in range(i+1, len(edges)):
            if not edges[i] in blacklist and not edges[j] in blacklist \
                    and not graph.edges_adjacent(edges[i], edges[j]) \
                    and graph.has_edge((edges[i][0], edges[j][1])) \
                    and graph.has_edge((edges[j][0], edges[i][1])):
                result.remove_edge(edges[i])
                result.remove_edge(edges[j])
                result.insert_edge((edges[i][0], edges[j][1]), graph.matrix[edges[i][0]][edges[j][1]])
                result.insert_edge((edges[j][0], edges[i][1]), graph.matrix[edges[j][0]][edges[i][1]])
                blacklist.append(edges[i])
                blacklist.append(edges[j])
                if sum_weight(graph_to_edges(result)) < sum_weight(highscore):
                    highscore = graph_to_edges(result)
    return highscore
