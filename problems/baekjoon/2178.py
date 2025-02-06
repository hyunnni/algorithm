import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip()))for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque([(0, 0)])

    while q:
        cx, cy, dist = q.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] == 1:
                maze[ny][nx] = maze[cy][cx] + 1 # 최단거리 저장
                q.append((nx, ny))

    return maze[N - 1][M - 1]   # (N - 1 , M - 1) 위치의 값이 최단거리

print(bfs())