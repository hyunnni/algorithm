import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
visited = [[False]*(m)for _ in range(n)]
count = 0
max_area = 0

def bfs(start):
    global max_area
    cur_area = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start_x, start_y = start
    visited[start_y][start_x] = True
    q = deque([start])

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):    
            nx, ny = cur_x + dx[i], cur_y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))
                cur_area += 1
    
    max_area = max(max_area, cur_area)

for y in range(n):
    for x in range(m):
        if grid[y][x] == 1  and not visited[y][x]:
            bfs((x, y))
            count += 1

print(count)
print(max_area)