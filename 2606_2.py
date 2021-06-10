from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        if check[node] == 0:
            check[node] = 1
            for t in graph[node]:
                queue.append(t)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
check = [0]*(N+1)
bfs(1)
print(sum(check)-1)