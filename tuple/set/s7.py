x = {1,2,3}
y = frozenset(x)
x.add(y)
print(x) # {frozenset({1, 2, 3}), 1, 2, 3}

x.remove(y)
print(x) # {1, 2, 3}

s = {1,2,3}
s.add(4)
print(s) # {1, 2, 3, 4} 

