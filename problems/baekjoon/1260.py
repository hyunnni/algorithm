import sys
from collections import deque
sys.setrecursionlimit(10000)

n, m, v  = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
dfs_result_list = []

def dfs(n):
    visited_dfs[n] = True
    dfs_result_list.append(n)

    for neighbor in graph[n]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

visited_bfs = [False] * (n + 1)
bfs_result_list = []

def bfs():
    queue = deque([v])
    visited_bfs[v] = True
    bfs_result_list.append(v)
    
    while queue:
        n = queue.popleft()
        for neighbor in graph[n]:
            if not visited_bfs[neighbor]:
                queue.append(neighbor)
                visited_bfs[neighbor] = True
                bfs_result_list.append(neighbor)
    
dfs(v)
bfs()

print(*dfs_result_list)
print(*bfs_result_list)