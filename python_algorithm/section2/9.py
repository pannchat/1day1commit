n = int(input())
arr=[]
tmp=0
res=0
for i in range(n):
    t = list(map(int,input().split()))
    t.sort()
    a,b,c = map(int,t)
    if a==b and b==c:
        tmp = 10000 + (a*1000)
    elif a==b or a==c:
        tmp = 1000 + (a*100)
    elif b==c :
        tmp = 1000 + (b*100)
    else:
        tmp =  c*100
    if tmp > res:
        res = tmp

print(res)