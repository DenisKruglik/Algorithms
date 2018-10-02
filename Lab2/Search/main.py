import random, timeit, searches

minVal = 0
maxVal = 1000000000


def generate_random_list(length):
    return sorted(random.sample(range(minVal, maxVal), length))


if __name__ == '__main__':
    k = 2
    prev = k

    while True:
        lst = generate_random_list(k)
        val = random.choice(lst)
        globs = {
            'searches': searches,
            'lst': lst,
            'val': val
        }
        bin_time = timeit.timeit('searches.bin_search(lst, val)', globals=globs)
        interpol_time = timeit.timeit('searches.interpolation_search(lst, val)', globals=globs)
        print('k =', k)
        print('Binary search time:', bin_time)
        print('Interpolation search time:', interpol_time)

        if bin_time > interpol_time:
            print('Answer: %d' % prev)
            break

        prev = k
        k += 1
