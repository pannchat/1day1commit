from collections import deque
n = int(input())
arr = []
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for _ in range(n):
    arr.append(list(map(int,input().split())))

ch = [[0]*n for _ in range(n)]
sum = 0
Q = deque()
ch[n//2][n//2] = 1
sum += arr[n//2][n//2]
Q.append((n//2, n//2))
L = 0

while True:
    if L == n//2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += arr[x][y]
                ch[x][y] = 1
                Q.append((x,y))
    L += 1
print(sum)

