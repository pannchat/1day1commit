def DFS(L):
    global cnt
    ch[L] = 1
    for i in range(1,n+1):
        if ch[i]==0 and arr[L][i] == 1:
            cnt += 1
            DFS(i)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    cnt=0
    arr = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        arr[a][b] = arr[b][a] = 1
    DFS(1)
    print(cnt)