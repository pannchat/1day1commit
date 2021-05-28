def DFS(L, sum):
    global res
    if L == n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1,sum+arr[L])
        DFS(L+1,sum-arr[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    s = sum(arr)
    res=set()
    DFS(0,0)
    print(s - len(res))
