def d1(para1,para2):
    
    return "para 1", para1, para2 

def d2():
    return "para 2"

def d3():
    return "para 3"

d = d1(d2(), d3())
print(d)  # ('para 1', 'para 2', 'para 3')


def d1(text):
    return text.upper()
def d2(text):
    return text.lower()
def d3(func):
    result = func("saisudhir")
    return result

d = d3(d1)
print(d) # SAISUDHIR
d = d3(d2)
print(d) # saisudhir

