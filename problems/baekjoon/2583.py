import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
grid = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
area_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sx, ex = x1, x2 - 1
    sy, ey = M - y2, M - y1 - 1
    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            grid[y][x] = 1

def bfs(sx, sy):
    area = 1
    visited[sy][sx] = True
    q = deque([(sx, sy)])
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[ny][nx] and grid[ny][nx] == 0:
                    visited[ny][nx] = True
                    area += 1
                    q.append((nx, ny))
        
    return area

for y in range(M):
    for x in range(N):
        if grid[y][x] == 0 and not visited[y][x]:
            area_list.append(bfs(x, y))

area_list.sort()
print(len(area_list))
print(*area_list)