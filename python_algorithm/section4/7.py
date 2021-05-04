n = int(input())
arr = list(map(int,input().split()))
m = int(input())
for _ in range(m):
    minx = min(arr)
    maxx = max(arr)
    for i in range(n):
        if arr[i] == minx:
            arr[i] += 1
            minx = None
        elif arr[i] == maxx:
            arr[i] -= 1
            maxx = None

print(max(arr)-min(arr))
