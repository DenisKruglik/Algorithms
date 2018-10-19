import shelve
from chain_collision_hash_table import ChainCollisionHashTable


data = shelve.open('data')['data']


def count_longest_chain(data, koef=ChainCollisionHashTable.A):
    longest = 0

    for dataset in data:
        htable = ChainCollisionHashTable(1000, koef)
        i = 0

        for val in dataset:
            htable.set(val)
            i += 1

        long_chain = htable.longest_chain()
        longest = long_chain if long_chain > longest else longest

    return longest


if __name__ == '__main__':
    longest_for_A = count_longest_chain(data)
    print("Longest chain for A:", longest_for_A)
    NA = 0.602214085774
    longest_for_NA = count_longest_chain(data, NA)
    print("Longest chain for NA:", longest_for_NA)
    ER = 0.6371
    longest_for_ER = count_longest_chain(data, ER)
    print("Longest chain for ER:", longest_for_ER)
    LOST = 0.4815162342
    longest_for_LOST = count_longest_chain(data, LOST)
    print("Longest chain for LOST:", longest_for_LOST)
