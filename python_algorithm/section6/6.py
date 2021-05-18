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
    n, m = map(int,input().split())
    arr = [0]*m
    cnt = 0
    DFS(0)

# 1 1 1
# 1 1 2
# 1 2 1
# 1 2 2
# 2 2 2
# 2 1 1
# 2 1 2
# 2 2 2