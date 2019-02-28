from frozendict import FrozenDict


def run(machine, word, ends=FrozenDict(y=True, n=False), start=0, empty=' ', log=False):
    state = 0
    pos = start
    word = {i: c for i, c in enumerate(word)}
    while True:
        if log: print(state, word.get(pos, empty), '->', end=' ')
        if state in ends:
            if log: print('end')
            return ''.join([word[i] for i in sorted(word)]).strip(empty), ends[state]
        state, char, move = machine[state][word.get(pos, empty)]
        if log: print(state, char, '+1' if move > 0 else move)
        word[pos] = char
        pos += move
