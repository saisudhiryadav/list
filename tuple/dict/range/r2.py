 # r = range(10)
 # r = range(1,20,2)
 # for i in r:
   # print(i,end = " ") # 1 3 5 7 9 11 13 15 17 19 
    
r1 = range(10)     
r1 = range(1,20,4)
for i in r1:
    print(i,end = " ") # 1 4 7 10 13 16 19 
    
    
def d1():
  x = 10
  print("scope: ", x)
  def d2():
    y = 20
    z = 30 
    print("scope: ", y)
    print("scope: ", z)
  return d2 
  