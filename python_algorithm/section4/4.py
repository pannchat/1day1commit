def Count(mid):
    cnt=1
    tmp = arr[0]
    for i in range(1,n):
        if arr[i]-tmp >= mid :
            cnt += 1
            tmp=arr[i]
    return cnt
n,c = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()

distance = 0
l =arr[0]
r=arr[-1]

while(l <= r):
    mid = (l+r)//2
    if Count(mid) >= c:
        res = mid
        l = mid + 1
    else:
        r = mid - 1

print(res)