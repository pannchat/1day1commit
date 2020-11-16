import sys
T = int(sys.stdin.readline())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, (
        sys.stdin.readline().split(' ')))

    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    if r1+r2 == distance or abs(r2-r1) == distance:
        print(1)
    elif r1+r2 < distance or distance < abs(r2-r1):
        print(0)
    else:
        print(2)
