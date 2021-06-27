
dx = [1,0,-1,0]
dy = [0,-1,0,1]
def DFS(x,y):
    global cnt
    if x == ex and y == ey :
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if  0<=xx<=n-1 and 0<= yy <= n-1 and ch[xx][yy] == 0  and arr[xx][yy] > arr[x][y]:
                ch[xx][yy] = 1
                DFS(xx,yy)
                ch[xx][yy] = 0

if __name__ == "__main__":
    n = int(input())
    arr = []
    ch = [ [0] * n for _ in range(n) ]
    min = 2147480000
    max = -2147480000
    for i in range(n):
        arr.append(list(map(int,input().split())))
        for idx,v in enumerate(arr[i]):
            if v < min:
                min = v
                sx = i
                sy = idx
            if v > max:
                max = v
                ex = i
                ey = idx
         
    ch[sx][sy] = 1
    cnt = 0
    DFS(sx,sy)
    print(cnt)
