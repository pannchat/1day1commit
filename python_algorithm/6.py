N = int(input())
T = list(map(int,input().split()))

def digit_sum(n):
    tmp=0
    while(n>0):
        tmp += n % 10
        n = n // 10
    return tmp
max = 0
for i in T:
    tot = digit_sum(i)
    if tot > max:
        max = tot
        res = i
print(res)