n = int(input())
# arr = [[0]*n for _ in range(n+1)]
arr = [list(map(int,input().split())) for _ in range(n)]
arr.insert(0, [0]*n)
arr.append([0]*n)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for x in arr:
    x.insert(0,0)
    x.append(0)
count = 0
for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        if all(arr[i][j] > arr[i+dx[k]][j+dy[k]] for k in range(4)):
            count += 1

print(count)