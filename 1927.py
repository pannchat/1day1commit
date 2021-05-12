import heapq as hq
import sys
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0 :
        if len(heap) == 0:
            print('0')
        else:
            print(hq.heappop(heap))
    elif x > 0:
        hq.heappush(heap, x)
