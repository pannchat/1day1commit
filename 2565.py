n = int(input())
dp= [1]*n
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int,input().split()))

arr.sort(key= lambda a: a[0] )
for i in range(1,MAX):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))