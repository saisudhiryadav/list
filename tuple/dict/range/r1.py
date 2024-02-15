r = range(10)
print(type(r)) # <class 'range'>

r1 = list(range(10))
print(r1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(r1)) # <class 'list'> 


def d1():
    
    print("d1 function")
    
    def d2():
        
        print("d2 funtion")
        
    return d2

d = d1()    
print(d)
print(d.__name__)
d()



def d1(a):
    def d2(b):
        return print(a+b)
    return d2

d= d1(10)
d(20)