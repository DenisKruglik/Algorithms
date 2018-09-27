import math, copy


def insertion_sort(arr, return_new=True):
    if return_new:
        a = copy.copy(arr)
    else:
        a = arr
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a


def quicksort(arr, p=0, r=-1, return_new=True):
    if p == 0 and r < 0 and return_new:
        a = copy.copy(arr)
    else:
        a = arr
    r = len(a) - 1 if r < 0 else r

    if p < r:
        q = partition(a, p, r)
        if p < q - 1:
            quicksort(a, p, q-1, False)
        if q < r:
            quicksort(a, q, r, False)
    return a


def partition(arr, left, right):
    i, j = left, right
    pivot = arr[math.floor((left + right) / 2)]

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return i


def hybrid_sort(arr, small, p=0, r=-1, return_new=True):
    if p == 0 and r < 0 and return_new:
        a = copy.copy(arr)
    else:
        a = arr
    r = len(a) - 1 if r < 0 else r

    if len(a[p:r+1]) <= small:
        a[p:r + 1] = insertion_sort(a[p:r+1], False)
        return a
    else:
        if p < r:
            q = partition(a, p, r)
            if p < q - 1:
                hybrid_sort(a, small, p, q - 1, False)
            if q < r:
                hybrid_sort(a, small, q, r, False)
        return a
