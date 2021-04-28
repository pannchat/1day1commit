def count(len):
    cnt=0
    for i in lan:
        cnt+=(i//len)
    return cnt

n,k = map(int,input().split())
lan = []

for i in range(n):
    lan.append(int(input()))
res=0
largest = max(lan)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if count(mid) >= k:
        res = mid
        lt = mid+1

    else:
        rt = mid-1
print(res)