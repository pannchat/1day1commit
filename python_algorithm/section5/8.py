n = int(input())
arr=[]
for i in range(n):
    arr.append(input())
else:
    for i in range(n-1):
        arr.remove(input())
print(arr[0])