n,k = map(int, input().split())
coin = []
count = 0
for _ in range(n):
    coin.append(int(input()))


for i in range(len(coin)-1,-1,-1):
    count += k // coin[i]
    k = k - k // coin[i] * coin[i]
    
print(count)