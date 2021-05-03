#2중 반복문 비효율적
n = int(input())
arr = []
cnt=0
for _ in range(n):
    arr.append(list(map(int,input().split())))
for t,w in arr:
    for i in range(n):
        if arr[i][0] > t and arr[i][1] > w:
            break
    else:
        cnt += 1
        print([t,w])
print(cnt)
