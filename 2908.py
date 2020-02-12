import sys
a,b  = map(str,sys.stdin.readline().split())
a_rev =''
b_rev = ''

for i in a:
    a_rev = i + a_rev
for i in b:
    b_rev = i + b_rev

a = int(a_rev)
b = int(b_rev)
if a>b:
    print(a)
else:
    print(b)