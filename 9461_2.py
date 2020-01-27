import sys
arr = [0] * 100
arr[0:4] = 1,1,1,2,2
T = int(sys.stdin.readline())

for i in range(5,100):
    arr[i] = arr[i-1] + arr[i-5]

for j in range(0,T):
    N = int(sys.stdin.readline())
    print(arr[N-1])