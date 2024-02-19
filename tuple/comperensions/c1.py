l = [i for i in range(1,10)]
print(l)
l1 = [i**2 for i in range(1,10)]
print(l1)

names = ["sai","sai","sudhir","yadav"]
l2 = [i if i == "sai" else "not sai" for i in names]
print(l2) # ['sai', 'sai', 'not sai', 'not sai']

l3 = [x+y for x in [10,20,30] for y in [5,10]]
print(l3) # [15, 20, 25, 30, 35, 40]

l4 = []
for i in [10,20,30]:
    for j in [5,10]:
        l4.append(i+j)
print(l4) # [15, 20, 25, 30, 35, 40]




       
        
