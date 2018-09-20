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
        if left[0][key] <= right[0][key]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    elif len(right) > 0:
        result.extend(right)
    return result


# def parallel_merge_sort(l1, k1, l2, k2):
#     if len(l1) <= 1:
#         return l1
#     else:
#         middle = math.floor(len(l1) / 2)
#         left = parallel_merge_sort(l1[:middle], k1, l2, k2)
#         right = parallel_merge_sort(l1[middle:], k1, l2, k2)
#         return parallel_merge(left, right, l2, k2)
#
#
# def parallel_merge(left, right, l2, k2):
#     left2 = []
#     right2 = []
#     for i in left:
#         for j in l2:
#             if j[k2] == i[k2]:
#                 left2.append(j)
#                 break
#
#     for i in right:
#         for j in l2:
#             if j[k2] == i[k2]:
#                 right2.append(j)
#                 break
#
#     return (left2, r)
