def DFS(L,s,sum):
    global res
    if sum > m:
        return
    if L == n :
        if res < s :
            res = s
        return
    else:
        DFS(L+1, s+arr[L][0], sum + arr[L][1])
        DFS(L+1, s, sum)

if __name__ == "__main__":
    n, m = map(int,input().split())
    arr=[]
    res = 0

    for _ in range(n):
        a,b = map(int,input().split())
        arr.append([a,b])
    # arr.sort()

    DFS(0,0,0)
    print(res)