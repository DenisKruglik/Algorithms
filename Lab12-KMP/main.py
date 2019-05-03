import tkinter as tk, re
from tkinter import simpledialog


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


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Substring search')
    root.geometry("1000x300+300+250")
    state = 0
    input_str = ''
    label = tk.Label(text=input_str, justify=tk.LEFT)

    def onkeypress(event):
        if re.match('^[a-zA-Z0-9]*$', event.char):
            global state, label, input_str
            state = dfa[state].get(event.char, 0)
            if state == pat_size:
                state = 0
                label.config(text=input_str[:-pat_size+1], textvariable=None)
                input_str = ''
                tk.Label(text=pattern, justify=tk.LEFT, fg='red').pack(side=tk.LEFT)
                label = tk.Label(textvariable=input_str, justify=tk.LEFT)
                label.pack(side=tk.LEFT)
            else:
                input_str += event.char
                label.config(text=input_str)

    root.bind('<KeyPress>', onkeypress)
    label.pack(side=tk.LEFT)
    pattern = simpledialog.askstring('Pattern', 'Enter search pattern')
    pat_size = len(pattern)
    dfa = build_dfa(pattern)
    root.mainloop()
