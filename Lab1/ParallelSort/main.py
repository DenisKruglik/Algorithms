import shelve

data = shelve.open('data')
first = data['first']
second = data['second']
