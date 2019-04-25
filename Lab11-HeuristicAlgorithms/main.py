from sortings import hybrid_sort as hsort
import re
from fractions import Fraction
from math import inf


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
                graph[i][j] = inf

