"""
Itertools: product, permutations, combinations,
accumulate, groupby and infinite iterators

Collection of tools for handling iterators(data types that can be used in a for loop
"""

"""
from itertools import product

a = [1, 2]
b = [2, 4]
prod = product(a, b)
print(list(prod))  # generates a cartesian number for each number of the lists
prod = product(a, b, repeat=2)
print(list(prod))  # generates a cartesian number for each number of the lists
"""

"""
from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
# perm = permutations(a, 2)  # only with two elements from the array
print(list(perm))  # like a permutation in mathematics
"""

"""
from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
# no repetitions
comb = combinations(a, 2)  # all possible combinations with the specific group
print(list(comb))  # like a combinations in mathematics

# with repetitions
comb_wr = combinations_with_replacement(a, 2)  # all possible combinations with the specific group
print(list(comb_wr))  # like a combinations in mathematics
"""

"""
from itertools import accumulate

import operator  # for multiply instead of sum

a = [i for i in range(1, 6)]
acc = accumulate(a)
print(list(acc))
acc = accumulate(a, func=operator.mul)  # a simple way to factorial a number
print(a)
print(list(acc))  # gets the sum of the elements
"""

"""
from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
# group_obj = groupby(a, key=smaller_than_3)
# group_obj = groupby(a, key=lambda x: x < 3)  # with lambda func(small oneline function)
#
# for key, value in group_obj:
#     print(key, list(value))

persons = [{'name': 'Tim', 'age': 15},
           {'name': 'Tony', 'age': 18},
           {'name': 'Tomas', 'age': 18},
           {'name': 'Thiago', 'age': 55}
           ]

# this will group the elements by their ages
group_obj = groupby(persons, key=lambda x: x['age'])  # with lambda func(small oneline function)
for key, value in group_obj:
    print(key, list(value))
"""
from itertools import count, cycle, repeat

# count
# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# cycle
# a = [1, 2, 3]
# for i in cycle(a):
#     print(i)
#     if i == 3:
#         break

# repeat
for i in repeat(2, 10):  # repeats the first parameter how many the second one is
    print(i)

