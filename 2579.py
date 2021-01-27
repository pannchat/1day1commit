import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(301)]
li = [0 for i in range(301)]
for i in range(N):
    li[i] = int(input())
dp[0] = li[0]
dp[1] = li[0] + li[1]
dp[2] = max(li[1]+li[2], li[0]+li[2])

for i in range(3, N):
    dp[i] = max(dp[i-3]+li[i-1]+li[i], dp[i-2]+li[i])
print(dp[N-1])
