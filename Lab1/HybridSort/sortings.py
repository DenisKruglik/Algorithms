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
        q = random_pivot_partition(a, p, r)
        quicksort(a, p, q-1, False)
        quicksort(a, q+1, r, False)
    return a


def random_pivot_partition(array, start, end):
    pivot = random.randint(start, end)
    array[end], array[pivot] = array[pivot], array[end]
    return findq(array, start, end)


def findq(array, start, end):
    pivot = end
    partition_index = start

    for i in range(start, end):
        if array[i] < array[pivot]:
            array[partition_index], array[i] = array[i], array[partition_index]
            partition_index += 1

    array[pivot], array[partition_index] = array[partition_index], array[pivot]
    return partition_index


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
            q = random_pivot_partition(a, p, r)
            hybrid_sort(a, small, p, q - 1, False)
            hybrid_sort(a, small, q + 1, r, False)
        return a


if __name__ == '__main__':
    arr = [6, 1, 9, 3, 2, 0, 4, 5, 8, 7]
    b = quicksort(arr)
    print(b)
