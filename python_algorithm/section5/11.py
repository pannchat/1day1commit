import heapq
heap = []
while True:
    
    x = int(input()) 
    if x > 0 :
        heapq.heappush(heap, x)
    elif x == 0 :
        print(heap)
        print(heapq.heappop(heap))
        heap = []
    elif x == -1:
        break
    

