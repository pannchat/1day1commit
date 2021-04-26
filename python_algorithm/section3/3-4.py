arr = [i for i in range(21)]

for i in range(10):
    a,b = map(int,input().split())
    arr[a:b+1] = arr[b:a-1:-1]

[print(s,end=" ") for s in arr[1:]]
