import sys
n = int(sys.stdin.readline())
room = [[0]*2 for _ in range(n)]

for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    room[i][0] = x
    room[i][1] = y

room = sorted(room, key=lambda a: a[0])
room = sorted(room, key=lambda a: a[1])
cnt = 0
end = 0


for i,j in room:
    if i >= end:
        cnt += 1
        end = j

print(cnt)