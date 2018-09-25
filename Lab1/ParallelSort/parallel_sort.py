import math


def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        middle = math.floor(len(arr) / 2)
        left = merge_sort(arr[:middle], key)
        right = merge_sort(arr[middle:], key)
        return merge(left, right, key)


def merge(left, right, key):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0][0][key] <= right[0][0][key]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    elif len(right) > 0:
        result.extend(right)
    return result


def parallel_merge_sort(l1, k1, l2, k2):
    l2.sort(key=lambda x: x[k2])
    grouped_second = group_by_values(l2, k2)
    list_to_sort = join(l1, grouped_second, k2, 'val')

    sorted_list = merge_sort(list_to_sort, k1)
    first_sorted = [i[0] for i in sorted_list]
    second_sorted = []

    for i in sorted_list:
        if i[1] is not None:
            second_sorted.extend(i[1]['data'])

    return first_sorted, second_sorted


def group_by_values(lisst, key):
    result = []
    prev = None
    buffer = []

    for i in lisst:
        if prev is None:
            buffer.append(i)
            prev = i
        elif prev[key] == i[key]:
            buffer.append(i)
        else:
            result.append({'val': prev[key], 'data': buffer})
            buffer = []
            buffer.append(i)
            prev = i

    if len(buffer): result.append({'val': buffer[0][key], 'data': buffer})

    return result


def join(l1, l2, k1, k2):
    result = []

    for i in l1:
        corresponding_group_list = list(filter(lambda x: x[k2] == i[k1], l2))
        corresponding_group = corresponding_group_list[0] if len(corresponding_group_list) else None
        result.append((i, corresponding_group))

    return result
