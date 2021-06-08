
def DFS(v):
    ch[v] = 1
    print(v ,end =' ')
    for i in range(1,n+1):
        if ch[i]==0 and arr[v][i]==1 :
            DFS(i)
def BFS(v):
    ch[v] = 0
    Q = [v]
    while Q:
        v = Q.pop(0)
        print(v, end=' ')
        for i in range(1,n+1):
            if (ch[i]==1 and arr[v][i]==1):
                Q.append(i)
                ch[i]=0

if __name__ == "__main__":
    n,m,v = map(int,input().split())
    arr = [[0]*(n+1) for i in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        arr[a][b] = arr[b][a] = 1
    ch = [0] * (n+1)
    DFS(v)
    print()
    BFS(v)
    
