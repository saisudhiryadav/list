# b = bytes((1,2,3,4))
# print(b)

# b1 = bytes({55:1,65:2,75:3})
# print(b1) # b'7AK'

l = [1,2,3,4,5]
b = bytes(l)
for i in b:
    print(i,end = " ") # 1 2 3 4 5 
