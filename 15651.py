import sys
def DFS(L):
    if L == m :
        [print(arr[i], end=" ") for i in range(m)]
        print("")
        return
    else:
        for i in range(1,n+1):
            arr[L] = i
            DFS(L+1)

    

if __name__ == "__main__":
    n, m = map(int,sys.stdin.readline().split())
    arr = [0] * m
    DFS(0)