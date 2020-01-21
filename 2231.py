import sys
def solve(n):
    start = n - len(str(n)) * 9
    start = 1 if start < 1 else start
    for i in range(start, n):
        _sum = i
        _sum += sum(map(int, str(i)))
        if _sum == N:
            print(i)
            return
    print(0)

N = int(sys.stdin.readline())
solve(N)