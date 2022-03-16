"""
Dictionary:
Key-Value pairs, Unordered, Mutable
"""

# Ways to create a dict
mydict = {"name": "Tony", 'age': 20, 'city': 'São Vicente'}
# print(mydict)
"""
mydict2 = dict(name='tony', age=20, city='Santos')
print(mydict2)
"""

# Access dict values
"""
name = mydict['name']
lastname = mydict['lastname']  # this will run an exception, because there's no key with this name
print(name)
"""

# Change dict values or create another kay-value pair
"""
mydict['name'] = "Anthony"
mydict['lastname'] = "Nunes"
"""

# Delete itens
"""
del mydict['lastname']
mydict.pop('age')
mydict.popitem()  # this removes last item and returns it
"""

# Check whether the key-value exists
"""
if 'lastname' in mydict:
    print(mydict['name'])
else:
    print('no, theres any key with this name')

try:
    print(mydict['lastname'])
except:
    print('No, theres any key with this name')
"""

# Loop through a dict
"""
for key in mydict:
    print(key)

print('')

for key in mydict.keys():  # does the same thing as the previous
    print(key)

print('')

for value in mydict.values():
    print(value)

# both in one loop
for key, value in mydict.items():
    print(key, ':', value)
"""

# Copying a dict
"""
mydict_copy = mydict  # careful with this, because if you change the copy, the original one will be changed too
mydict_copy["name"] = "Batata"
print(mydict_copy)
print(mydict)
"""

# actual copy
"""
mydict_copy = mydict.copy()
mydict_copy["name"] = "Batata"
print(mydict_copy)
print(mydict)
"""
# or dict build-in function
"""
mydict_copy = dict(mydict)
mydict_copy["name"] = "Batata"
print(mydict_copy)
print(mydict)
"""

# Merge two dicts

# when they don't have same keys
"""
mydict2 = {"lastname": "Nunes", 'email': 'anthony@email.com', 'status': 'online'}
mydict.update(mydict2)
print(mydict)
"""

# when they have same keys
"""
mydict3 = {"name": "Batata", 'age': 20, 'email': 'potato@coldmail.com'}
mydict.update(mydict3)
print(mydict)
"""

# KeyTypes

# Numbers
"""
mydict = {3: 9, 6: 36, 9: 81}
value = mydict[0]  # this is not a list, is a dict, so call with the key not the index
value = mydict[3]
print(value)
"""

# Tuples
"""
mytuple = (8, 7)
mydict = {mytuple: 15}  # the sum
print(mydict)
"""

# Lists is not allowed
"""
mylist = [8, 7]  # will run a error
mydict = {mylist: 15}  # the sum
print(mydict)
"""
