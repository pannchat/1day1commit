def Count(mid):
    sum=0
    cnt=1
    for i in arr:
        if sum + i > mid:
            cnt += 1
            sum = i
        else:
            sum+=i
    return cnt

n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
l=1
r=sum(arr)
res=0
while(l<=r):
    mid = (l+r)//2
    if Count(mid) <= m:
        res= mid
        r = mid - 1
    else:
        l = mid + 1

print(res)

