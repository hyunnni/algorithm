import sys
from collections import deque

N = int(input())
grid = [list(map(int, sys.stdin.readline().strip()))for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
complex_list = []

def bfs(sx, sy):
    count = 1
    visited[sy][sx] = True
    q = deque([(sx, sy)])

    while q:
        cx, cy = q.popleft()
    
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and grid[ny][nx] == 1:
                    q.append((nx, ny))
                    visited[ny][nx] = True
                    count += 1

    return count

for y in range(N):
    for x in range(N):
        if not visited[y][x] and grid[y][x] == 1:
            complex_list.append(bfs(x, y))

complex_list.sort()
print(len(complex_list))
print(*complex_list, sep='\n')