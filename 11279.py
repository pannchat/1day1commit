import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == -1 :
        break
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-hq.heappop(heap))
    else:
        hq.heappush(heap, -x)


        