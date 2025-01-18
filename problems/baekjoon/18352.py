import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[]for _ in range (n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def bfs(start):
    distances = [-1]*(n+1)
    queue = deque([start])
    distances[start] = 0
    
    while queue:
        cur = queue.popleft()

        for neighbor in graph[cur]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[cur] + 1
                queue.append(neighbor)
    
    return distances

distances = bfs(x)

result = [i for i in range(1, n+1) if distances[i] == k]

if result:
    print('\n'.join(map(str,result)))
else:
    print(-1)