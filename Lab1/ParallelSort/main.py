import shelve, parallel_sort

data = shelve.open('data')
first = data['first']
second = data['second']
first, second = parallel_sort.parallel_merge_sort(first, 'code', second, 'order')
print(first, second, sep='\n')
