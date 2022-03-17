"""
String: Ordered, immutable, text representation
"""

# To use quotes inside of it, use backslash
"""
mystr = 'Batata\'s potato'
my_str = "Hello World. I'm a programmer"
print(mystr)
print(my_str)
"""

# for multiline strings
# mytext = """
# Poteito
# Potato, \
# same thing
# """

# print(mytext)

# for substrings
"""
string = 'This is a text'
# letter
char = string[0]

# word (slice a string)
word = string[0:5]

print(char)
print(word)

# changing string content

# string[0] = "A"  # strings are immutable, so this will run an error
# print(string)


# reverse a string
reversed = string[::-1]
print(reversed)
"""

# Concatenate strings
"""
name = 'Tony'
lastname = 'nunes'

fullname = name + ' ' + lastname
print(fullname)
"""

# Iterating a string
"""
alphabet = "abcde"

for letter in alphabet:
    print(letter)
"""

# Check if a char is inside a string
"""
word = 'anthony'
if 'a' in word:
    print('a' in word)
"""

# Removing white spaces from start and end
"""
my_string = '         lot of spaces       '
without_space = my_string.strip()
print(my_string)
print(without_space)
"""

# converting to uppercase and lowercase
"""
string = 'Anthony'
print(string.upper())
print(string.lower())
"""

# Check if a string starts or ends with a specific char or string
"""
string = 'Anthony'
print(string.startswith('A'))  # case sensitive
print(string.startswith('a'))  # case sensitive
print('\n')
print(string.endswith('Y'))  # case sensitive
print(string.endswith('y'))  # case sensitive
"""

# find the index of a char or substring
"""
string = 'Anthony'
print(string.find('thony'))  # finds the first index that it finds with
print(string.find('ba'))  # returns -1 if not find anything
"""

# count how many times a substring appears
"""
string = 'anthony'
print(string.count('n'))
"""
# replace char or substring
"""
string = 'batata'
print(string.replace(string[0], string[0].upper()))
"""

# convert String to list
"""
string = 'a simple phrase'
string_listed = string.split()  # deafult: ' '
print(string)
print(string_listed)

# convert back to string
new_string = ' '.join(string_listed)
print(new_string)
"""

# Performance
"""
from timeit import default_timer as timer

my_list = ['a'] * 1000000
# print(my_list)
my_string = ''

# Bad
start = timer()
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)

# Good (faster)
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)
# print(my_string)
"""

# Formatting strings
"""
# Olds styles %, .format()
var = 'Tony'
my_string = 'The variable is %s' % var
print(my_string)

var = 3
my_string = 'The variable is %d' % var
print(my_string)

var = 3.1415679
my_string = 'The variable is %.10f' % var
print(my_string)

var = 3.1415679
my_string = 'The variable is {}'.format(var)
print(my_string)

var = 3.1415679
var2 = 6
my_string = 'The variable is {:.2f} and {}'.format(var, var2)
print(my_string)

# New f-Strings
var = 'Tony'
var2 = 'nunes'
my_string = f'The variable is {var} {var2.replace(var2[0], var2[0].upper(), 1)}'
print(my_string)
"""
