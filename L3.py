l1 = 'l=[1,2,3]'
import timeit
print(timeit.timeit(l1)) # 0.05959179997444153

t1 = 't=(1,2,3)'
import timeit
print(timeit.timeit(t1)) # 0.01612889999523759

l = ["sai"]
l.append("sudhir")
print(l)

l = ["sai","yadav"]
l.insert(1,"sudhir")
print(l) # ['sai', 'sudhir', 'yadav']

