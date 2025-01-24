import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

# 간선 정보, 양방향 그래프 생성
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드 오름차순 정렬 -> 작은 번호부터 방문 보장
for i in range(n + 1):
    graph[i].sort()

# DFS
def dfs(start):
    visited[start] = True
    result.append(start)

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(neighbor)

# BFS 
def bfs(start):
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

# DFS 실행
visited = [False] * (n + 1)
result = []
dfs(v)
print(*result)

# BFS 실행
visited = [False] * (n + 1)
print(*bfs(v))