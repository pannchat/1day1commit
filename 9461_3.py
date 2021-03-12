t = int(input())
arr = [0]*100
arr[0:10] = [0,1,1,1,2,2,3,4,5,7,9]
for _ in range(t):
    n = int(input())
    for i in range(5,n+1):
        arr[i]=arr[i-2] + arr[i-3]
    print(arr[n])