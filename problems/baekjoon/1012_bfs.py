import sys
from collections import deque

def bfs(grid, sx, sy):
    q = deque([(sx, sy)])
    grid[sy][sx] = 0

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == 1:
                grid[ny][nx] = 0
                q.append((nx, ny))
                
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    grid = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        grid[y][x] = 1
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1:
                cnt += 1
                bfs(grid, x, y)
    print(cnt)