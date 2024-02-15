t1 = (1,2,3,4)
print(t1+(5,6)) # (1, 2, 3, 4, 5, 6)

t = 1,2,3,4,5,6,7
  # 0 1 2 3 4 5 6        
print(t[2:5]) # (3, 4, 5)

l = list("hello")
print(l)


t1,*t2 = (1,2,3,4,5)
print(t1) # 1
print(t2) # [2, 3, 4, 5]
 
 
t1,*t2,t3,t4 = (1,2,3,4,5)
print(t1) # 1
print(t2) # [2, 3]
print(t3) # 4

s = {1,2,3,'one',5,'two'}
print(s)
print(type(s)) # {1, 2, 'two', 3, 5, 'one'}
             # {'two', 1, 2, 3, 'one', 5}