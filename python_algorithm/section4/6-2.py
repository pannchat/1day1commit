n = int(input())
arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(reverse=True)
largest = 0
cnt=0
for t,w in arr:
    if largest < w :
        largest = w
        cnt += 1
print(cnt)