# Tuple: ordered, immutable, allows duplicate elements

mytuple = ('Tony', 20, 'California')

"""
# Ways to create a tuple
mytuple = ('Tony', 20, 'California')

# It's still a tuple even without parenteses (they're optional)
mytuple = 'Tony', 20, 'California'

# or use the built-in tuple function with an iterable(ex: list)
mytuple = tuple(['Tony', 20, 'California'])
"""

"""
# if you put only one element, it becomes a string
mytuple = ("Tony")
print(type(mytuple))

# to consider it as a tuple use a coma (,) in the end
mytuple = ('Tony',)
print(type(mytuple))
"""

"""
# get an element from a tuple
item = mytuple[0]
print(item)

# you can specify with negative numbers as well
item = mytuple[-1]  # get last item
print(item)
"""

# trying to change tuple's element
# mytuple[0] = 'nunes'  # it will generate an error, because tuples are immutable

# Iterate a tuple
"""
for item in mytuple:
    print(item)
"""

# Check whether an element is inside a tuple
"""
if 'Batata' in mytuple:
    print('Yeah')
else:
    print('Oh no')
"""

"""
my_tuple = ('a', 'n', 't', 'h', 'o', 'n', 'y')

# Checking how many items is in a tuple
print(len(my_tuple))


# Count how many times an element is in a tuple
print(my_tuple.count('n'))

# Find the first index of specific element
print(my_tuple.index('n'))  # if search for an element that is not in a tuple, it will generate an error
"""

"""
# Convert tuple into a list and vise versa
mylist = list(mytuple)
print(type(mylist))

my_tuple = tuple(mylist)
print(type(my_tuple))
"""

"""
# Slicing tuples

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]  # it will get the last index - 1 instead
print(b)

# same thing with lists
c = a[2:]  # from the second index to the end
print(c)

d = a[:3]  # from the third index to the beginning
print(d)

e = a[::3]  # with steps (-1 for reverse)
print(e)
"""

"""
# Unpacking tuples

print(mytuple)

# the number of elements must match with the tuple length
name, age, city = mytuple  # typing on the left side
print(name)
print(age)
print(city)

# Unpacking with star

my_tuple = (0, 1, 2, 3, 4, 5, 6)

first, *middle, end = my_tuple

print(first)  # this comes as a number
print(middle)  # it comes as a list
print(end)
"""

"""
# Comparing sizes between tuple and list
import sys

my_tuple = ('Tony', 20, 'California')
my_list = ['Tony', 20, 'California']
# get the size in bytes
print('List: ', sys.getsizeof(my_list), 'bytes')
print('Tuple: ', sys.getsizeof(my_tuple), 'bytes')
# Result: tuples are lighter


# Iterate and create lists and tuples
import timeit

# use a statement(stmt) and repeats a certain number os times to get the time to do the statement
print(timeit.timeit(stmt='[0, 1, 2, 3, 4, 5]', number=1000000))
print(timeit.timeit(stmt='(0, 1, 2, 3, 4, 5)', number=1000000))
# Result: tuples are faster/efficient
"""

