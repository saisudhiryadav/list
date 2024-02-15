def d1(a,b):
    return print(a+b)

d1(10,20)

l1 = lambda a,b : a+b
l = l1(10,20)
print(l) #  30  

def d2(a=10,b=20):
    return print(a+b)
d2()

l2 = lambda a=10,b=20: a+b
l = l2(10,20)
print(l)

def d1(a):
    def d2(b):
        return print(a+b)
    return d2
d = d1(10)
d(15)
  
  
l5 = lambda a : (lambda b : print(a+b))
l = l5(10)
l(15)
