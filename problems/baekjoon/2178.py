import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip()))for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque([(0, 0, 1)])
    visited[0][0] = True

    while q:
        cx, cy, dist = q.popleft()
        if cx == M - 1 and cy == N - 1:
            return dist
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if maze[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny, dist + 1))

print(bfs())