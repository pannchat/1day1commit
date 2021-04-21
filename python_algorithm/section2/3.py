N,K = map(int, input().split())
card = list(map(int,input().split()))
res = set()
for i in range(N):
    for j in range(i+1,N):
        for t in range(j+1,N):
            res.add(card[i] + card[j] + card[t])

res = list(res)
res.sort(reverse=True)
print(res[K-1])