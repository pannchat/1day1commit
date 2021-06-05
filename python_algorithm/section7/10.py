dx = [1,0,-1,0]
dy = [0,-1,0,1]

def DFS(x,y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and arr[xx][yy] == 0:
                arr[xx][yy] = 1
                DFS(xx,yy)
                arr[xx][yy] = 0
if __name__ == "__main__":
    arr = []
    cnt = 0
    for _ in range(7):
        arr.append(list(map(int,input().split())))
    arr[0][0] = 1
    DFS(0,0)
    print(cnt)
