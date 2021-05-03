L = list(map(int, input().split()))
sum=0
for now in L:
    sum+=abs(now)
print(sum)