import sys
n,m = map(int,sys.stdin.readline().split())
map_list = []
# for i in range(0,m):
#     for j in range(0,n):

    
for i in range(0,m):
    map_list.append(list(map(int,sys.stdin.readline().split())))

# 지도 출력
for i in range(0,n):
    for j in range(0,m):
        print(map_list[i][j] ,end=' ')
        if j == m-1 :
            print("")

for i in range(0,n):
    for j in range(0,m):
        if map_list[i][j] == 2:
            k=j
        elif map_list[i][j] == 1:
            t=i
        
            for _ in map_list[i]
                if map_list[i][j] == 0: