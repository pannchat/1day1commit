import copy

# test1 = (1,2)
# test2 = copy.deepcopy(test1)
# test3 = copy.copy(test1)
# print(id(test1), id(test2),id(test3))

# test3 = [3,4]
# test4 = copy.deepcopy(test3)
# test5 = copy.deepcopy(test3)
# print(id(test3), id(test4), id(test5))

# a = (1,2,['a','b'])
# b = copy.deepcopy(a)
# c = a[:]
# d = copy.copy(c)

# print(id(a),id(b),id(c),id(d))

class A:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return id(self.x) == id(other.x)


x = [1]
a= A(x)
b= A(a.x)
c= A(x[:])
d= A(a.x[:])

print(a==b, b==c, c==d)
# print(a,b,c,d)