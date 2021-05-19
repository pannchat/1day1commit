import sys
def DFS(L,sum):
    global res
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum + arr[i])
            
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    m = int(input())
    res = 214700000
    DFS(0,0)
    print(res)