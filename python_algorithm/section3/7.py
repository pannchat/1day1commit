n = int(input())
arr =[]
MAX = 0
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
    if sum1 > MAX:
        MAX = sum1
    if sum2 > MAX:
        MAX = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += arr[i][i]
    sum2 += arr[i][n-i-1]
if sum1 > MAX:
    MAX = sum1
if sum2 > MAX:
    MAX = sum2
print(MAX)