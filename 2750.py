import sys
list=[]
N = int(sys.stdin.readline())

for i in range(0,N):
    list.append(int(sys.stdin.readline()))

for i in range(1,N):
    for j in range(i,0,-1):
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break
for i in list:
    print(i)