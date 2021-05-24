

if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = [[0] * n for _ in range(n)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        arr[a-1][b-1] = c
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
