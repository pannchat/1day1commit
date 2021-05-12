import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []
while(True):
    x = int(sys.stdin.readline())
    if x == -1 :
        break
    if x == 0:
        if len(heap) == 0:
            print('-1')
        else:
            print(-hq.heappop(heap))
    else :
        hq.heappush(heap, -x)


