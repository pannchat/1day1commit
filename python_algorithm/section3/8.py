n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
val = 0
s=e=n//2
for i in range(n):
    for j in range(s,e+1):
        val += arr[i][j]
    if i < n//2 :
        s-=1
        e+=1
    else:
        s +=1
        e -=1
print(val)