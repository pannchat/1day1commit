a = [0, [1, [2, [3,[4,[5,None]]]]]]
b = [6,[7,[8,[9,[10,[11, None]]]]]]
c = a


while c:
    c[0] = a[0] + b[0]
    c = c[1]
    b = b[1]
    a = a[1]
    print(c[0])

print(c)
while c :
    print(c[0], end='')
    c = c[1]
