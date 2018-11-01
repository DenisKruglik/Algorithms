from graph.adjacency_list_graph import AdjacencyListGraph
import algorithms


graph = AdjacencyListGraph()
options = [
    'Insert vertex',
    'Insert edge',
    'Remove vertex',
    'Remove edge',
    'Clear',
    'Print graph',
    'Euler cycle search',
    'Check to which connected component vertex belongs',
    'Check if graph is bipartite and show parts',
    'Exit'
]


def select(message, options):
    prompt = message + '\n'

    for i, o in enumerate(options):
        prompt += "\t" + str(i+1) + ". " + o + '\n'

    prompt += '\n'
    return input(prompt)


def insert_vertex():
    key = input("Enter vertex key: ")
    graph.insert_vertex(key)


def insert_edge():
    v1 = input('Enter first incident vertex key: ')
    v2 = input('Enter second incident vertex key: ')
    graph.insert_edge([v1, v2])


def remove_vertex():
    key = input("Enter vertex key: ")
    graph.remove_vertex(key)


def remove_edge():
    v1 = input('Enter first incident vertex key: ')
    v2 = input('Enter second incident vertex key: ')
    graph.remove_edge([v1, v2])


def clear():
    graph.clear()


def print_graph():
    for k in graph.adjacency_lists:
        print(k + ': ', end='')
        for v in graph.adjacency_lists[k]:
            print(v + ' ', end='')
        print('\n')


def euler():
    cycle = algorithms.euler_cycle_search(graph)
    if cycle is not None:
        print(cycle)
    else:
        print("There's no Euler cycle in this graph")


def connected_components():
    components = []
    all_vertices = set()

    while all_vertices != set(graph.adjacency_lists):
        start = list(set(graph.adjacency_lists) - all_vertices)[0]
        bfs = algorithms.breadth_first_search(graph, start)
        components.append(bfs)

        for i in bfs:
            all_vertices.add(i)

    for i, c in enumerate(components):
        print('Component ' + str(i) + ': ', end='')
        for v in c:
            print(v + ' ', end='')
        print('\n')


def bipartite():
    all_vertices = set()
    first_part = []
    second_part = []

    while all_vertices != set(graph.adjacency_lists):
        start = list(set(graph.adjacency_lists) - all_vertices)[0]
        marked, is_bipartite = algorithms.breadth_first_search(graph, start, True)
        if is_bipartite:
            for v in marked:
                all_vertices.add(v)
                if marked[v] % 2 == 0:
                    first_part.append(v)
                else:
                    second_part.append(v)
        else:
            print('Graph is not bipartite')
            break
    else:
        print('Graph is bipartite')
        print(first_part)
        print(second_part)


def ex():
    exit(0)


def action(ind):
    actions = {
        '1': insert_vertex,
        '2': insert_edge,
        '3': remove_vertex,
        '4': remove_edge,
        '5': clear,
        '6': print_graph,
        '7': euler,
        '8': connected_components,
        '9': bipartite,
        '10': ex
    }
    selected = actions.get(ind, None)
    if selected is None:
        print('Invalid option')
    else:
        selected()


if __name__ == '__main__':
    while True:
        action(select('Choose option', options))
