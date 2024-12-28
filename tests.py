from value import * 
a = Value(2, label='a')
b = Value(3, label='b')
c = Value(10, label='c')
d = a*b
e = d + c
print(d + c)
print(e._prev)
