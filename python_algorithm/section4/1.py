n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
for i in range(len(arr)):
    if arr[i] == m:
        print(i+1)
        break
