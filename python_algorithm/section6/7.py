n = int(input())
arr = list(map(int,input().split()))
m = int(input())
cnt = 0

while m != 0:
    if m >= arr[-1]:
        cnt += m // arr[-1]
        m = m % arr.pop()
    else:
        arr.pop()
print(cnt)


