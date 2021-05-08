import sys
from collections import deque
n,k=map(int,input().split())
dq = list(range(1,n+1))
dq = deque(dq)
cnt = 1
while(len(dq) != 1):
    for _ in range(k-1):
        tmp = dq.popleft()
        dq.append(tmp)
    else:
        dq.popleft()
print(dq[0])