import sys
def count_fib(n):
    zero_count = [1,0]
    one_count = [0,1]
    if n < 2 :
        return
    
    for i in range(2,n+1):
        zero_count.append(zero_count[i-2] + zero_count[i-1])
        one_count.append(one_count[i-2] + one_count[i-1])
    return zero_count, one_count

N = int(sys.stdin.readline())
zero_count, one_count = count_fib(40)
for _ in range(N):
    M = int(sys.stdin.readline())
    print("%d %d" % (zero_count[M],one_count[M]))