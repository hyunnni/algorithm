import sys
from collections import deque

N = int(input())
grid = [list(sys.stdin.readline().strip())for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ncb = 0
cb = 0

def bfs(sx, sy, blindness):
    q = deque([(sx, sy, grid[sy][sx])])
    visited[sy][sx] = True

    while q:
        cx, cy, color = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                if blindness and (color == grid[ny][nx] or (color in ['R','G']) and (grid[ny][nx] in ['R','G'])):
                    visited[ny][nx] = True
                    q.append((nx ,ny, color))

                elif not blindness and color == grid[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx ,ny, color))

for i in range(2):
    visited = [[False]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                bfs(x, y, i)
                if i == 0:
                    ncb += 1
                else:
                    cb += 1

print(ncb, cb)