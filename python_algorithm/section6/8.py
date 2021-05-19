def DFS(L):
    global cnt
    if L == m:
        cnt += 1
        [print(i, end=' ') for i in arr]
        print("")
        return
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                arr[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0


if __name__ == "__main__":
    n,m = map(int,input().split())
    ch = [0] * (n+1)
    arr = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)