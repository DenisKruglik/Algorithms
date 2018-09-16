import shelve, sortings, time, math
arrs = shelve.open('arrays')['arrays']


def measure_time(func, *argv, **argk):
    start = time.time()
    func(*argv, **argk)
    end = time.time()
    return end - start


def avg(vals):
    count = len(vals)
    sum = 0
    for i in vals:
        sum += i
    return sum / count


def count_avg_time(func, **additional):
    vals = []
    for arr in arrs:
        for i in range(50):
            vals.append(measure_time(func, arr, **additional, return_new=True))
    print('counted')
    return avg(vals)


def middle(vfrom, vto):
    diff = vto - vfrom
    add = math.floor(diff/2)
    return vfrom + add


if __name__ == '__main__':
    qt = count_avg_time(sortings.quicksort_iterative)
    nfrom = 7
    nto = 200
    n = middle(nfrom, nto)
    prev = n
    print('n =', n)

    while True:
        ht = count_avg_time(sortings.hybrid_sort_iterative, small=n)
        if ht <= qt:
            nfrom = n
        elif qt < ht:
            nto = n
        prev = n
        n = middle(nfrom, nto)
        print('n =', n)
        if abs(n - prev) <= 1 and ht < qt:
            break

    print('Answer:', n)
