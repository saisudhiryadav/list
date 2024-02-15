s = {1,1,2,2,3,3}
print(s) # {1, 2, 3}

s = {"sai","sudhir"}
s.update(["yadav"])
print(s) # {'yadav', 'sai', 'sudhir'}

l = [s]
print(l) # [{'sai', 'sudhir', 'yadav'}]

s1 = {1,2,3,4}
s1.remove(5)
#print(s1) # KeyError: 5
