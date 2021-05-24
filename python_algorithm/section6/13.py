def DFS(v):
    global cnt
    if v == n:
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            if arr[v][i] == 1 and ch[i] == 0:
                ch[v] = 1
                DFS(v+1)
                ch[v] = 0
            
            


if __name__ == "__main__":
    n,m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    ch = [0]*(n+1)
    cnt = 0
    for _ in range(m):
        a,b = map(int,input().split())
        arr[a][b] = 1
        ch[1] = 1
    DFS(1)
    print(cnt)


