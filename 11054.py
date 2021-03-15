n = int(input())
arr = (list(map(int,input().split())))
LIS = [1]*n
LDS = [1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            LIS[i] = max(LIS[i],LIS[j]+1)

arr.reverse()
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            LDS [i] = max(LDS[i],LDS[j]+1)
LDS.reverse()
result = [x+y for x,y in zip(LIS,LDS)]
print(max(result)-1)