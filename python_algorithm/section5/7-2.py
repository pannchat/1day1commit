import sys
from collections import deque
important = list(input())
n = int(input())

for i in range(n):
    plan = input()
    dq=deque(important)
    for j in plan:
        if j in dq:
            if j != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:  
            print("#%d NO" %(i+1))