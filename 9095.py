import sys
T = int(sys.stdin.readline())
dp = [1, 2, 4]

for i in range(T):
    N = int(sys.stdin.readline())
    if (N < 4):
        print(dp[N-1])
    else:
        for j in range(3, N):
            dp.append(dp[j-1]+dp[j-2]+dp[j-3])
        print(dp[-1])
        dp = [1, 2, 4]
