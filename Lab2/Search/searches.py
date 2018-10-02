def bin_search(lst, x):
    lower_bound = 0
    upper_bound = len(lst)
    while lower_bound != upper_bound:
        compared_value = (lower_bound + upper_bound) // 2
        if x == lst[compared_value]:
            return compared_value
        elif x < lst[compared_value]:
            upper_bound = compared_value
        else:
            lower_bound = compared_value + 1
    return None


def interpolation_search(lst, x):
    mid = None
    low = 0
    high = len(lst) - 1

    while lst[low] < x < lst[high]:
        mid = low + ((x - lst[low]) * (high - low)) // (lst[high] - lst[low])

        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid

    if lst[low] == x:
        return low
    elif lst[high] == x:
        return high
    else:
        return None
