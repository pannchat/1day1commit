n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
i = n - 1
count = 0
while(arr):
    if len(arr) == 1:
        count += 1
        break
    if arr[0] + arr[-1] > m:
        arr.pop()
        count += 1
    else:
        arr.pop(0)
        arr.pop()
        count += 1

print(count)
