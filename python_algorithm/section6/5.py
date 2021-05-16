def DFS(L, sum, tsum):
    global w
    if sum + (tot - tsum) < w:
        return
    if sum > c:
        return
    if L == n:
        if sum > w :
            w = sum
    else:
        DFS(L+1, sum+arr[L], tsum+arr[L])
        DFS(L+1, sum,tsum+arr[L])
if __name__ == "__main__":
    c, n = map(int,input().split())
    arr = []
    w=0
    for _ in range(n):
        arr.append(int(input()))
    
    tot = sum(arr)
    DFS(0,0,0)    
    print(w)


