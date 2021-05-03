n = int(input())
room=[]
for _ in range(n):
    room.append(list(map(int,input().split())))

room = sorted(room, key=lambda a : a[0])
room = sorted(room, key=lambda a : a[1])


cnt=0
et=0
for s,e in room:
    if s >= et:
        cnt += 1
        et=e
print (cnt)