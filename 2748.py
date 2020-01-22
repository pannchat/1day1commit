import sys
# n = int(sys.stdin.readline())

# def fib(n):
#     if n == 0 : return 0
#     if n == 1 : return 1
#     return fib(n-1)+fib(n-2)

# print(fib(n))
# 위는 Top-Down 방식. 재귀 시간초과

N = int(sys.stdin.readline())

def fib(n):
    fib_list=[0,1]
    for i in range(2,n+1) :
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    return fib_list[n]

print(fib(N))

# Bottom UP 방식