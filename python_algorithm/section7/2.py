def DFS(L,pay,time):
    global res
    if time > n-1:
        return 
    if L == n :
        if res < pay:
            res = pay
        return
    else:
        DFS(L+1, pay+p[L], time+t[L])
        DFS(L+1,pay,time)
if __name__ == "__main__":
    n = int(input())
    t = []
    p = []
    res=0
    for _ in range(n):
        x,y = map(int,input().split())
        t.append(x)
        p.append(y)
    DFS(0,0,0)
    print(res)