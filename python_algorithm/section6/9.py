import sys
def DFS(L,sum):
    if L == n and sum == m:
        sum = 0
        for i in arr:
            print(i ,end=' ')
        print("")
        sys.exit(0)
        return
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                arr[L] = i
                ch[i] = 1
                DFS(L+1 , sum+(arr[L]* b[L]))
                ch[i] = 0
if __name__ == "__main__":
    n, m = map(int,input().split())
    b = [1] * n
    for i in range(1,n):
        b[i] = b[i-1] * (n-i) // i

    arr = [0] * n
    ch = [0] * (n+1)
    DFS(0,0)