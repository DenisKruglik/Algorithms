import math, copy, random


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


# Забыл, что у моего варианта quicksort, но пусть будет
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = math.floor(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    elif len(right) > 0:
        result.extend(right)
    return result


def quicksort(arr, p=0, r=-1, return_new=True):
    if p == 0 and r < 0 and return_new:
        a = copy.copy(arr)
    else:
        a = arr
    r = len(a) - 1 if r < 0 else r
    if p < r:
        q = findq(a, p, r)
        quicksort(a, p, q-1, False)
        quicksort(a, q+1, r, False)
    return a


def quicksort_iterative(arr, p=0, r=-1, return_new=True):
    if p == 0 and r < 0 and return_new:
        a = copy.copy(arr)
    else:
        a = arr
    r = len(a) - 1 if r < 0 else r
    stack = [p, r]
    while len(stack) > 0:
        r = stack.pop()
        p = stack.pop()
        q = findq(a, p, r)
        if q-1 > p:
            stack.append(p)
            stack.append(q-1)
        if q+1 < r:
            stack.append(q+1)
            stack.append(r)
    return a


def findq(a, p, r):
    x = a[random.randint(p, r)]
    q = p
    for i in range(p, r):
        if a[i] <= x:
            a[i], a[q] = a[q], a[i]
            q += 1
    a[q], a[r] = a[r], a[q]
    return q


def hybrid_sort(arr, small, p=0, r=-1, return_new=True):
    if p == 0 and r < 0 and return_new:
        a = copy.copy(arr)
    else:
        a = arr
    r = len(a) - 1 if r < 0 else r

    if len(a) <= small:
        return insertion_sort(a, False)
    else:
        if p < r:
            q = findq(a, p, r)
            hybrid_sort(a, small, p, q - 1, False)
            hybrid_sort(a, small, q + 1, r, False)
        return a


def hybrid_sort_iterative(arr, small, p=0, r=-1, return_new=True):
    if p == 0 and r < 0 and return_new:
        a = copy.copy(arr)
    else:
        a = arr
    r = len(a) - 1 if r < 0 else r
    if len(a) <= small:
        return insertion_sort(a, False)
    else:
        stack = [p, r]
        while len(stack) > 0:
            r = stack.pop()
            p = stack.pop()
            q = findq(a, p, r)
            if q - 1 > p:
                if q - p <= small:
                    a[p:q] = insertion_sort(a[p:q])
                else:
                    stack.append(p)
                    stack.append(q - 1)
            if q + 1 < r:
                if r - q <= small:
                    a[q+1:r+1] = insertion_sort(a[q+1:r+1])
                else:
                    stack.append(q + 1)
                    stack.append(r)
        return a
