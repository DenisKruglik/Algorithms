import math


def horse(x, y, first_call=True):
    if first_call:
        horse.solutions = [[None] * (y+1) for x in range(x+1)]
        horse.solutions[0][0] = 1

    if horse.solutions[x][y] is not None:
        return horse.solutions[x][y]

    result = 0

    if x - 2 >= 0 and y - 1 >= 0:
        result += horse(x - 2, y - 1, False)

    if x - 1 >= 0 and y - 2 >= 0:
        result += horse(x - 1, y - 2, False)

    return result


def subsequence(seq):
    length = len(seq)
    lens = [1] * length
    prevs = [None] * length

    for i in range(1, length):
        greatest = 0
        ind = None
        for j in range(i):
            if greatest < seq[j] <= seq[i]:
                greatest = lens[j]
                ind = j
        if ind is not None:
            lens[i] = lens[ind] + 1
            prevs[i] = ind

    current = lens.index(max(lens))
    result = [seq[current]]

    while prevs[current] is not None:
        prev = prevs[current]
        result.insert(0, seq[prev])
        current = prev

    return result


def palindrome(string):
    l = len(string)
    lens = [[0] * l for i in range(l)]
    for i in range(l):
        lens[i][i] = 1

    greatest = 1

    for i in range(1, l):
        for j in range(l - i):
            end = i + j
            start = j
            if len(string[start:end + 1]) == 2:
                if string[start] == string[end]:
                    lens[end][start] = 2
                else:
                    lens[end][start] = 1
            else:
                if string[start] == string[end]:
                    lens[end][start] = lens[end - 1][start + 1] + 2
                else:
                    lens[end][start] = max(lens[end-1][start], lens[end][start+1])

            greatest = lens[end][start] if lens[end][start] > greatest else greatest

    return greatest


def knapsack(weights, costs, amounts, capacity):
    n = len(weights)
    d = [[0] * (capacity+1) for i in range(n)]

    for i in range(n):
        for c in range(1, capacity + 1):
            d[i][c] = d[i - 1][c]
            for l in range(min(amounts[i], math.floor(c / weights[i])), 0, -1):
                d[i][c] = max(d[i][c], d[i - 1][c - l * weights[i]] + costs[i] * l)

    return _restore_items(n-1, capacity, d, weights, costs)


def _restore_items(k, s, d, weights, costs, result=None):
    if result is None:
        result = [0] * len(d)
    if d[k][int(s)] == 0:
        return result
    if d[k - 1][int(s)] == d[k][int(s)]:
        _restore_items(k - 1, s, d, weights, costs, result)
    else:
        prev = d[k - 1][int(s)] if k > 0 else 0
        amount = (d[k][int(s)] - prev) / costs[k]
        _restore_items(k - 1, s - weights[k] * amount, d, weights, costs, result)
        result[k] = int(amount)
    return result
