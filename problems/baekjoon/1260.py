import sys
from collections import deque

n, m, v  = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def dfs(start, graph, visited):
    result = []
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        result.append(node)
        for neighbor in reversed(graph[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    
    return result

def bfs(start, graph, visited):
    result = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs_result_list = dfs(v, graph, visited_dfs)
bfs_result_list = bfs(v, graph, visited_bfs)

print(*dfs_result_list)
print(*bfs_result_list)