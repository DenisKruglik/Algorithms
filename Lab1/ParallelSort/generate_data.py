import shelve, random, string

firstRecCount = 20
secondRecCount = 26
codeLen = 10
firstList = []
secondList = []
for i in range(firstRecCount):
    firstRec = {
        'order': i,
        'code': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(codeLen))
    }
    firstList.append(firstRec)

for i in range(secondRecCount):
    secondRec = {
        'order': random.randint(0, firstRecCount-1),
        'letter': chr(ord('A') + i)
    }
    secondList.append(secondRec)

data = shelve.open('data')
random.shuffle(firstList)
random.shuffle(secondList)
data['first'] = firstList
data['second'] = secondList
data.close()
