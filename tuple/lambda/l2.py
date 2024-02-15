import sys
s = sys.getrecursionlimit()
print(s) # 1000 

i = 0 
def d1():
    global i
    i = i+1
    print("d1 function", i)
    d1()
    
d1()    



def factorial(n):
    
    if n == 1:
        print(n)
        return 1
    else: 
        print(n)
        return n * factorial(n-1)
    
r = factorial(5)
print(r)
   