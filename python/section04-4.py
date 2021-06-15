dic = {'name' : 'park', 'phone': '010-1234-1234', 'birth' : 920123, 'list':[1,2,3], 'tuple':(1,2,3)}
print(dic)

print(dic['name'])
# print(dic['nickname'])
print(dic.get('name'))
print(dic.get('nickname'))

dic['new'] = '새로운 요소'
print(dic.keys())
print(list(dic.keys()))

print(dic.values())
print(list(dic.values()))

print(dic.items())
print(list(dic.items()))

a = set()
b = set("Hello")
c = set([1,4,5,6,6])
print(type(a))
print(b)
print(c)

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s1-s2)
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))

# s1.update([7,8])
s1.update((7,8))
print(s1)
s1.remove(7,8)
print(s1)