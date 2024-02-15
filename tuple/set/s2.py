s = {1,2,3,4}
s.remove(4)
print(s) # {1, 2, 3} 

s1 = {1,2,3,4,5}
s1.discard(6)
print(s1) # {1, 2, 3, 4, 5}

# s2 = {1,2,3,4,5,6}
# s2.remove(7)
# print(s2) # KeyError: 7


# s3 = {1,2,3,4}
# s3.clear(2)
# print(s3) # TypeError: set.clear() takes no arguments (1 given)

s4 = {1,2,3,4}
s4.clear()
print(s4) # set()


