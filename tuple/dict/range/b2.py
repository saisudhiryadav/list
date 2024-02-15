b = bytearray([1,2,3])
b.reverse()
print(b) # bytearray(b'\x03\x02\x01')
b.append(5)
print(b) # bytearray(b'\x01\x02\x03\x05')

l = [10,20,30]
b1 = bytearray(l)
print(b1[1]) # 20
print(b1[2]) # 30

z = b[0] = 40
print(z)