"""
Set(Conjuntos): Unordered, mutable, no duplicates
"""

# Ways to create a set
"""
myset = {1, 2, 3}  # -> {1, 2, 3}
print(myset)

# no duplicates
myset = {1, 2, 3, 2, 1}  # -> {1, 2, 3}
print(myset)

myset2 = set([1, 2, 3, 4])
print(myset2)

myset3 = set("Hello")  # the output will be unordered
print(myset3)

# empty set
myset = {}  # careful
print(type(myset))  # -> dict

myset = set()
print(type(myset))  # -> set
"""

# Add and Remove elements to a set
"""
myset = set()

myset.add(6)
myset.add(1)
myset.add(4)
print(myset)

# myset.remove(3)  # if the element is not in the set, it runs an error

# myset.discard(2)  # this doesn't run error if not found

print(myset.pop())  # pops a random item from the set

# myset.clear()  # clear all

print(myset)
"""

# Iterate a set
"""
myset = {1, 2, 3, 4}

for call_it_anything in myset:
    print(call_it_anything)

# Check whether an element is inside a set
if 5 in myset:
    print("Yep")
else:
    print('No')
"""

# Merge sets (Like in math at Set Theory)
"""
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union combines without duplications
union = odds.union(evens)
print(union)

# intersection return only the item that exists in both sets
intersection = odds.intersection(evens)  # set()
print(intersection)

intersection = odds.intersection(primes)  # -> 3, 5, 7
print(intersection)
"""

# Diferences
"""
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

differenceA = setA.difference(setB)  # shows only elements that exist in A but not in B
differenceB = setB.difference(setA)  # shows only elements that exist in B but not in A

print(differenceA)
print(differenceB)

# This returns all the elements they don't have in common
diff = setA.symmetric_difference(setB)
diff_2 = setB.symmetric_difference(setA)  # same thing as the previous
print(diff)
print(diff_2)
"""
# obs: These previous methods do not change the original sets


# Update sets
# in these case, it changes the setA
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# update with union
"""
setA.update(setB)  
print(setA)
"""

# update with intersection
"""
setA.intersection_update(setB)
print(setA)
"""
# update with difference
"""
setA.difference_update(setB)
print(setA)
"""

# update with symmetric difference
"""
setA.symmetric_difference_update(setB)
print(setA)
"""

# Sup set, Super set and disjoint methods
"""
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8, 9}
print(setA.issubset(setB))  # -> False
print(setB.issubset(setA))  # -> True

print('')

print(setA.issuperset(setB))  # -> True
print(setB.issuperset(setA))  # -> False

print('')

# Calculate if two sets are disjoint
# Disjoint: returns True if both sets have no intersections (no same elements)
print(setA.isdisjoint(setB))  # -> False because they have elements in common
print(setA.isdisjoint(setC))  # -> True because they do not have elements in common
"""

# Copying sets
myset = {1, 2, 3}

# Wrong way
"""
myset_copy = myset  # careful with this
myset_copy.add(5)  # it will change the original set too
print(myset)
print(myset_copy)
"""

# Right way
"""
myset_copy = myset.copy()
myset_copy.remove(3)
print(myset)
print(myset_copy)

print('')

# or
myset_copy = set(myset)
myset_copy.discard(2)
print(myset)
print(myset_copy)
"""

# Frozen set (immutable version of a set)
"""
a = frozenset([1, 2, 3, 4])

a.add(2)  # error
a.remove(1)  # error
# And any updates will run an error

# obs: Union, difference and intersection are allowed

print(a)
"""