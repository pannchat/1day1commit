from queue import LifoQueue, Queue

def foo(n,x:list):
    q = Queue()
    q.put(n)
    while not q.empty():
        m = q.get()
        if m < len(x):
            q.put(x[m])
        print(m, end='')


foo(2,['tes',1])

# q [1]
# m = 1
# 1 < 3:
# q[3]
