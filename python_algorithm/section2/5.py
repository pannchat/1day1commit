N,M = map(int,input().split())
array=[0]*(N+M+10)

for i in range(1,N+1):
    for j in range(1,M+1):
        array[i+j] += 1

for i in range(N+M+1):
    if(array[i] == max(array)):
        print(i ,end=" " )
print("")