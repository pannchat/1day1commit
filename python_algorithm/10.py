n = int(input())
arr = list(map(int,input().split()))
tmp = 0
score = 0
for i in arr:
    if i == 1 :
        tmp += 1
        score += tmp
    else:
        tmp = 0

print(score)