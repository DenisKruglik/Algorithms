import readchar, sys


def build_dfa(pattern):
    alphabet = set(pattern)
    dfa = [{char: None for char in alphabet} for letter in pattern]
    for i, letter in enumerate(pattern):
        for char in alphabet:
            if char == letter:
                dfa[i][char] = i + 1
            else:
                lps = 0
                temp = pattern[:i] + char
                for j in range(1, i):
                    if temp[:j] == temp[-j:]:
                        lps = j
                dfa[i][char] = lps
    return dfa


def substring(string, dfa):
    state = 0
    end = len(dfa)
    for i, char in enumerate(string):
        state = dfa[state].get(char, 0)
        if state == end:
            return i - state + 1
    return -1
