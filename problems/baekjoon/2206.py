import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
map_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def bfs():
    visited = [[[False] * 2 for _ in range (m)] for _ in range(n)]
    queue = deque([(0, 0, 1, 0)])
    visited[0][0][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        curx, cury, dist, wall_break = queue.popleft()

        if curx == m - 1 and cury == n - 1 :
            return dist
        
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if map_list[ny][nx] == 0 and not visited[ny][nx][wall_break]:
                    visited[ny][nx][wall_break] = True
                    queue.append((nx, ny, dist + 1 , wall_break))
            
                if map_list[ny][nx] == 1 and wall_break == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    queue.append((nx, ny, dist + 1, 1))

    return -1

print(bfs())