N = int(input())


arr = [True for i in range(N+1)]
count = 0
for i in range(2, N+1):
    if arr[i] == True:
        count+=1
        for j in range(i+i ,N+1 , i):
            arr[j] = False

print(count)
