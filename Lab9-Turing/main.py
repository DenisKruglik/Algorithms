from interpreter import run


def task1_23():
    machine = {
        0: {
            'a': (1, ' ', 1),
            'b': (5, ' ', 1),
            ' ': ('y', 'a', 0)
        },
        1: {
            'a': (1, 'a', 1),
            'b': (1, 'b', 1),
            ' ': (2, ' ', -1)
        },
        2: {
            'a': (4, ' ', -1),
            'b': (3, ' ', -1),
            ' ': ('y', 'a', 0)
        },
        3: {
            'a': (3, ' ', -1),
            'b': (3, ' ', -1),
            ' ': ('n', ' ', 0)
        },
        4: {
            'a': (4, 'a', -1),
            'b': (4, 'b', -1),
            ' ': (0, ' ', 1)
        },
        5: {
            'a': (5, 'a', 1),
            'b': (5, 'b', 1),
            ' ': (6, ' ', -1)
        },
        6: {
            'a': (3, ' ', -1),
            'b': (4, ' ', -1),
            ' ': ('y', 'a', 0)
        }
    }
    print('Task 1.23')
    word = input('Enter an input word: ').strip().lower()
    result, answer = run(machine, word, log=True)
    if answer:
        print('The word is a palindrom, result -', result)
    else:
        print('The word is not a palindrom, result -', result)


def task2_2():
    machine = {
        0: {
            'f': (0, 'f', 1),
            'h': (0, 'h', 1),
            ' ': ('y', ' ', 0),
            'p': (1, 'p', 1)
        },
        1: {
            'p': (1, 'p', 1),
            'f': (0, 'f', 1),
            ' ': ('y', ' ', 0),
            'h': (2, 'h', -1)
        },
        2: {
            'p': (3, 'f', 1)
        },
        3: {
            'h': (4, ' ', 1)
        },
        4: {
            'p': (4, 'p', 1),
            'h': (4, 'h', 1),
            'f': (4, 'f', 1),
            ' ': (5, ' ', -1)
        },
        5: {
            ' ': ('y', ' ', 0),
            'h': (6, ' ', -1),
            'p': (7, ' ', -1),
            'f': (8, ' ', -1)
        },
        6: {
            'h': (6, 'h', -1),
            'p': (7, 'h', -1),
            'f': (8, 'h', -1),
            ' ': ('y', 'h', 0)
        },
        7: {
            'h': (6, 'p', -1),
            'p': (7, 'p', -1),
            'f': (8, 'p', -1),
            ' ': ('y', 'p', 0)
        },
        8: {
            'h': (6, 'f', -1),
            'p': (7, 'f', -1),
            'f': (8, 'f', -1),
            ' ': ('y', 'f', 0)
        }
    }
    print('Task 2.2')
    word = input('Enter an input word: ').strip().lower()
    result, answer = run(machine, word, log=True)
    print('Result:', result)


if __name__ == '__main__':
    task1_23()
    task2_2()