import sys

def padovan(n):
    arr=[1,1,1,2,2]
    if n < 6 :
        return arr[n-1]
    for i in range(5,n+1):
        arr.append(arr[i-1]+arr[i-5])
    return str(arr[n-1])

M = int(sys.stdin.readline())
arr = []
for i in range(M):
    arr.append(int(sys.stdin.readline()))
    print(padovan(arr[i]))
