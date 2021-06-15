a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'apple', 'banana']
e = [10, 100, ['apple', 'banana']]

print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

print(d[0:2])
print(e[2][0:3])

print(c + d)
print(c * 3)
# print(c * 1.5)
# print( d[2] * d)

c[0] = 123
print(c)

c[1:2] = [7,77,777]
print(c)
c[1] = [12,34]
print(c) 
del c[0]
print(c)
del c[0:2]
print(c)

listX = [1,5,4,2,3]
listX.append(9)
print(listX)

listX.insert(2,7)
print(listX)
listX.sort()
print(listX)

listX.sort(reverse=True)
print(listX)

listX.reverse()
print(listX)

listX.remove(7)
print(listX)

listX.pop(1)
print(listX)

ex = [99,88]
listX.extend(ex)
print(listX)

tp = ()
tp2 = (1,)
tp3 = (1,2,3)
tp4 = 1,2,3
tp5 = (1,2,3,(4,5,6))
# del tp2[0]

print(tp4)

print(tp5[1])
print(tp5[3][2])
print(tp5[1:3])

print(tp5.index(3))