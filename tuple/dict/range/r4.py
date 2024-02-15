def d1(func):
    
    def d2(a,b):
        
        return print(func(a+b))
    return d2


# without decorators
def d3(c):
    return c 

d = d1(d3)
d(10,10) # 20

# with decorators
@d1
def d4(d):
    return d
d4(10,10) # 20




