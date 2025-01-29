import sys
from collections import deque

def bfs(map, rain, startx, starty):
    queue = deque([(startx, starty)])
    visited[starty][startx] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        curx, cury = queue.popleft()
        for dx, dy in directions:
            nx, ny = curx + dx, cury + dy

            if 0 <= nx < n and 0 <= ny < n and map[ny][nx] > rain and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))

n = int(sys.stdin.readline())
height_map = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
max_height = max(map(max, height_map))

answer = 1
for rain in range(1, max_height):
    visited = [[False] * n for _ in range (n)]
    cnt  = 0

    for y in range(n):
        for x in range(n):
            if not visited[y][x] and height_map[y][x] > rain:
                bfs(height_map, rain, x, y)
                cnt += 1
    
    if cnt == 0:
        break

    answer = max(answer, cnt)

print(answer)