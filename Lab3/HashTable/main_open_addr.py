import shelve, random
from open_addressing_hash_table import OpenAddressingHashTable


data = shelve.open('data')['data']
worst = 0

for arr in data:
    htable = OpenAddressingHashTable(len(arr))

    for v in arr:
        tries = htable.set(v)
        worst = tries if tries > worst else worst

print("Max tries during insertion:", worst)
