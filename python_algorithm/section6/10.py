def DFS(L,s):
    global cnt
    if L == m:
        [ print(i, end=' ') for i in arr[:L]]
        print()
        cnt += 1
    else:
        for i in range(s,n+1):
            arr[L] = i
            DFS(L+1, i+1)

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = [0]*(n+1)
    cnt = 0
    DFS(0,1)
    print(cnt)