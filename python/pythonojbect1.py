print('EX1-1 : ')
print(dir())

x = {'name':'kim', 'age':33, 'city':'Seoul'}
y = x
y['name'] = 'park'
print(x,y, sep="\n")
print('EX2-1 : ', id(x), id(y))
print('EX2-2 : ', x == y) # 같은 value(값)을 가지고 있는지
print('EX2-3 : ', x is y) # 같은 object(객체)를 가리키고 있는지?

x['class'] = 10
print(x,y, sep="\n")

z = {'name':'park', 'age':33, 'city':'Seoul', 'class':10}
print('EX2-6', x, z, sep="\n")
print('EX2-7', x is z)
print('EX2-7', x == z)

tuple1 = (10,15,[1,2])
tuple2 = (10,15,[1,2])
print('EX3-1 : ', id(tuple1), id(tuple2))
print('EX3-1 : ', tuple1 is tuple2)
print('EX3-1 : ', tuple1 == tuple2)
print('EX3-1 : ', tuple1.__eq__(tuple2))

tl1 = [10,[100,105],(5,10,15)]
print('리스트', id(tl1[1]))
print('튜플', id(tl1[2]))
tl2 = tl1
tl3 = list(tl1)
print(id(tl1), id(tl1[1]), id(tl1[2]))
print(id(tl3), id(tl3[1]), id(tl3[2]))
# 4390070528 4389788928 4389535104
# 4390071936 4389788928 4389535104
print('EX4-1 : ', tl1 == tl2) 
print('EX4-2 : ', tl1 is tl2)
print('EX4-3 : ', tl1 == tl3)
print('EX4-4 : ', tl1 is tl3)

tl1.append(1000)
tl1[1].remove(105)
print('리스트', id(tl1[1]))

print('EX4-5 : ', tl1)
print('EX4-6 : ', tl2)
print('EX4-7 : ', tl3)


tl1[1] += [110,120]
tl2[2] += (110,120)
print('EX4-5 : ', tl1)
print('EX4-6 : ', tl2)
print('EX4-7 : ', tl3)

print('튜플', id(tl1[2]), tl3[2])


import copy
class Bascket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)
    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


bascket1 = Bascket(['Apple', 'Bag', 'Tv', 'Snack', 'Water'])
bascket2 = copy.copy(bascket1)
bascket3 = copy.deepcopy(bascket1)

print('EX5-1 : ', id(bascket1), id(bascket2), id(bascket3))
print('EX5-1 : ', id(bascket1._products), id(bascket2._products), id(bascket3._products))

bascket1.put_prod('Orange')
bascket2.del_prod('Snack')
print('EX5-2 : ', id(bascket1._products), id(bascket2._products), id(bascket3._products))


def add(x,y):
    x += y
    return x

x = 10
y = 5

print(add(x,y), x, y)

a = [10, 100]
b = [5, 10]

print(add(a,b), a, b) #원본의 주소 , 레퍼런스 주소를 넘겨서 원본이 수정된다.
c=(10,100)
d=(5,10)

print(add(c,d), c, d) # (10, 100, 5, 10) (10, 100) (5, 10)

tt1 = (1,2,3,4,5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 : ', tt1 is tt2, id(tt1), id(tt2))
print('EX7-1 : ', tt1 is tt3, id(tt1), id(tt3))


tt4 = (10,20,30,40,50)
tt5 = (10,20,30,40,50)

ss1 = {'test':'test'}
ss2 = {'test':'test'}

print('EX7-3 : ', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 : ', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))