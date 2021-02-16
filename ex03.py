N,M,K = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
first = data[N-1]
second = data[N-2]

count = int(M / ( K + 1)) * K
count += M % ( K + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (M - count) * second

print(result)