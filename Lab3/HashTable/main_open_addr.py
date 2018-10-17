import shelve
from open_addressing_hash_table import OpenAddressingHashTable


data = shelve.open('data')['data']
worst = 0

for arr in data:
    htable = OpenAddressingHashTable(len(arr))

    for k, v in enumerate(arr):
        tries = htable.set(k, v)
        worst = tries if tries > worst else worst

print("Max tries during insertion:", worst)