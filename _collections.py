"""
Coleections:
Counter, namedtuple, OrderedDict, default, deque
"""

"""
from collections import Counter

a = "aaabbbbccccc"

my_counter = Counter(a)
"""

"""
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
"""

"""
print(my_counter.most_common(1))  # get the element(s) that most appears at the string
# print(my_counter.most_common(2))  # test it

print(list(my_counter.elements()))
"""

"""
from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(10, 2)
print(pt.x, pt.y)
"""

"""
from collections import OrderedDict

ordered_dict = OrderedDict()
# ordered_dict = {}  # this also works  

ordered_dict['a'] = 1
ordered_dict['d'] = 4
ordered_dict['b'] = 2
ordered_dict['c'] = 3

print(ordered_dict)
"""

"""
# create a dafault type in case an Error occurs
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['c'])  # this returns a default value for integer, once the parameter put was int
"""


"""
from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([4, 5, 6])
d.extendleft([4, 5, 6])
print(d)

d.rotate(3)  # negative to rotate to left
print(d)
"""