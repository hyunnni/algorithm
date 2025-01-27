import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        
        for c in graph[node]:
            if not visited[c]:
                visited[c] = True
                queue.append((c))

connected_component = 0
for i in range(1, n+1):
    if not visited[i]:
        connected_component+=1
        bfs(i)

print(connected_component)