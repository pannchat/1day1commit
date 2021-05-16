import sys
def DFS(L, sum):
    if sum > tot//2 : 
        return
    if L == n:
        if sum == (tot - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+arr[L])
        DFS(L+1, sum)
if __name__ == "__main__":

    n = int(input())

    arr = list(map(int,input().split()))
    tot = sum(arr)
    DFS(0,0)
    print("NO")

