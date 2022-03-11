# code based on this video: https://www.youtube.com/watch?v=HGOBQPFzWKo&t
# exercices to fix the learning: https://wiki.python.org.br/ListaDeExercicios

'''================================='''
# Lists
'''================================='''

# ways to create a list
mylist = ['batata', 'cenoura', 'batavo']
print(mylist)

'''
mylist2 = list()
print(mylist2)
'''

# the first item of a list, it begins in zero 0
'''
item = mylist[0] # -> batata
'''

# get last item regardless the length of the list
'''
item2 = mylist[-1] # -> batavo
print(item2)
'''

# iterate a list (you can give any name to 'i' variable
'''
for i in mylist:
    print(i)
'''

# Check if something is inside a list
'''
if 'banana' in mylist:
    print('yes!!')
else:
    print('no :(')
    '''

# check the length of a list
'''
print(len(mylist))
'''

# add something to the list at the last position
'''
mylist.append('abacate')
print(mylist)
'''

# add something in a specific position list.insert(Index, something)
'''
mylist.insert(1, 'beterraba')
print(mylist)
'''

# remove last item and returns it
# if you want to remove a specific index, use: list.pop(index)
'''
lastItem = mylist.pop(0)
print(lastItem)
'''

# remove specific element without returning any value
'''
item = mylist.remove('cenoura')
print(item)
'''

# Clear the list
'''
mylist.clear()
print(mylist)
'''

# Reverse the list
'''
mylist.reverse()
'''

# Sort the list (alphabetical and numerical order)
# this change the original list
'''
mylist.sort()
'''

# create a new list sorted without change the original
'''
sorted_list = sorted(mylist)
print(sorted_list)
'''

# create a list with the same elements multiple times
'''
mylist = [0] * 5
print(mylist)
'''

# concatenate two lists
'''
mylist2 = [1,2,3,4,5]

new_list = mylist + mylist2

print(new_list)
'''

# Slice lists
# gets all elements from the first index to the second one, but it catches the last index - 1

a = mylist[0:2] # -> ['batata', 'cenoura']
print(a)