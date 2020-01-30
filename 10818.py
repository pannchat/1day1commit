import sys
n = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

print("%d %d" %(min(arr),max(arr)))
