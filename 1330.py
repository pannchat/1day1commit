import sys
n=list(map(int,sys.stdin.readline().split()))

if n[0] > n[1]:
    print(">")
elif n[0] < n[1] :
    print("<")
else:
    print("==")