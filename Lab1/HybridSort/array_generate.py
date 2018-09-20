import shelve, random

arrCount = 50
arrLen = 100000
maxVal = 1000000000
filename = 'arrays'
arrs = []
for i in range(arrCount):
    arr = []
    for j in range(arrLen):
        arr.append(random.randint(0, maxVal))
    arrs.append(arr)
storage = shelve.open(filename)
storage['arrays'] = arrs
storage.close()
