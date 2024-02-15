def d1(func):
    def d2():
        return "hello",func()
    return d2

# without decorator
def d3():
    return "hi"

d = d1(d3)
print(d()) # ('hello', 'hi')

# with decorator
@d1
def d4():
    return "Hey"
d= d4(),d3() # (('hello', 'Hey'), 'hi')
print(d) # ('hello', 'Hey')