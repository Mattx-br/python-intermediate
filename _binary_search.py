"""

Binary Search

"""

import random
import time
# [1,3,6,7,9,12,13]

# implement naive search

def naive_search(some_list, target):
    for i in range(len(some_list)):
        if some_list[i] == target:
            return i

    return -1


def binary_search(some_list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(some_list) - 1

    if high < low:
        return -1
    # Get the mid point(average of the list)
    midpoint = (low + high) // 2

    if some_list[midpoint] == target:
        return midpoint
    elif target < some_list[midpoint]:
        new_high = midpoint - 1
        return binary_search(some_list, target, low, new_high)
    else:
        # if the target is greater than the midpoint
        new_low = midpoint + 1
        return binary_search(some_list, target, new_low, high)

# if you are running just this one file, only run whatever is under this section
if __name__ == '__main__':
    # l = [1, 3, 6, 7, 9, 12, 13]
    # target = 12
    # print(naive_search(l, target))

    # print(binary_search(l, target))
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    
    sorted_list = sorted(list(sorted_list))

    target_list = [random.randint(-3 * length, 3 * length) for _ in range(length)]

    start = time.time()
    for target in target_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f'Naive search time: {end - start} seconds')
    
    start = time.time()
    for target in target_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f'Binary search time: {end - start} seconds')