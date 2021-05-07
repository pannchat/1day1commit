n, k = map(int,input().split())
arr = [i for i in range(1,n+1)]
i = 0
cnt = 1
while(len(arr)!=1):
    if i > len(arr)-1:
        i = 0

    if cnt == 3:
        arr.pop(i)
        cnt = 1
    else:
        cnt += 1
        i+=1

print(arr[0])
