import sys
a,b,c = map(int,sys.stdin.readline().split())
test = max(a,b,c)
if test == a:
    print(max(b,c))
elif test == b:
    print(max(a,c))
else :
    print(max(a,b))