import sys
from collections import deque

N = int(input())
grid = [list(sys.stdin.readline().strip())for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ncb = 0
cb = 0

def bfs(sx, sy):
    q = deque([(sx, sy, grid[sy][sx])])
    visited[sy][sx] = True

    while q:
        cx, cy, color = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
               if color == grid[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx ,ny, color))

# 일반 BFS 실행
visited = [[False]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(x, y)
            ncb += 1

# 적록색약 실행 위해 변환
for y in range(N):
    for x in range(N):
        if grid[y][x] == 'R':
            grid[y][x] = 'G'

# 적록색약 BFS 실행
visited = [[False]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(x, y)
            cb += 1  

print(ncb, cb)