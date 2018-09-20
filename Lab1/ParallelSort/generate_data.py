import shelve, random, string

recCount = 20
codeLen = 10
firstList = []
secondList = []
for i in range(recCount):
    firstRec = {
        'order': i,
        'code': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(codeLen))
    }
    firstList.append(firstRec)
    secondRec = {
        'order': i,
        'letter': chr(ord('A') + i)
    }
    secondList.append(secondRec)
data = shelve.open('data')
random.shuffle(firstList)
random.shuffle(secondList)
data['first'] = firstList
data['second'] = secondList
data.close()
