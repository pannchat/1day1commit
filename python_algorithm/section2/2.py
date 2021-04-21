T = int(input())
arr = []
for i in range(T):
    N,s,e,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = arr[s-1:e]
    arr.sort()
    print(arr[k-1])
