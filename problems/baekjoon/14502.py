import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

def bfs(graph):
    q = deque([(j, i) for i in range(n) for j in range(m) if graph[i][j] == 2])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                q.append((nx, ny))
    
    global answer
    count = sum([g.count(0) for g in graph])
    answer = max(answer, count)

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
x_y = [(x, y) for x in range(m) for y in range(n) if not graph[y][x]]
answer = 0

for c in combinations(x_y, 3):
    tmp_graph = deepcopy(graph)
    for x, y in c:
        tmp_graph[y][x] = 1
    bfs(tmp_graph)

print(answer)