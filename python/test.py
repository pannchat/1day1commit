a = [1, '2', 3, '4']
b = {1:'a', '2':'b', 3:'c', '4':'d'}

c = '.'.join([b[x] for x in a])
print(c)