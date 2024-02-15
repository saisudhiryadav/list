l = [1,2,3,4,5]
l[0:2] = [10,30]
print(l) # [10, 30, 3, 4, 5]

t = (1,)
print(type(t)) # <class 'tuple'>

t1 = (1,2,3,3,4,3)
print(t1.count(3)) # 3

t2 = (1,2,3,4,5)
print(t2[2]) # 3
