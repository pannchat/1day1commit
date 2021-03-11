import sys
n = map(int, sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
waiting_time=0
sum = 0
for i in arr:
    waiting_time += i
    sum += waiting_time

print(sum)