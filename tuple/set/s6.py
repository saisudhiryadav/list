s = {1,2,3,4}
s.add(5)
print(s) # {1, 2, 3, 4, 5}

s1 = {1,2,3,4,5,5,6,6,}
s2 = frozenset(s1)
print(s1) # {1, 2, 3, 4, 5, 6}

x = {1,2,3,4,5}
y = frozenset(x)
y.add(6)
print(y) # AttributeError: 'frozenset' object has no attribute 'add'

