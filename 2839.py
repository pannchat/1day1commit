import sys

N = int(sys.stdin.readline())
count = 0
while True:
    if(N % 5 == 0):
        count += N//5
        break
    elif(N < 0):
        count = -1
        break
    N -= 3
    count += 1

print(count)
