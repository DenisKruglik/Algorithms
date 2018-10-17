import random, shelve

data = [[random.randint(0, 1000) for j in range(1000)] for i in range(50)]
storage = shelve.open('data')
storage['data'] = data
storage.close()
