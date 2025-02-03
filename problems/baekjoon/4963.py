import sys
from collections import deque

def count_island(w, h, grid):
    """BFS를 사용하여 섬의 개수 세는 함수"""

    dx = [0, 0, 1, -1, 1, -1, 1, -1]  # 상, 하, 좌, 우, 대각선
    dy = [1, -1, 0, 0, 1, 1, -1, -1]

    visited = [[False] * w for _ in range(h)]  # 방문 여부 체크

    def bfs(start):
        """BFS를 사용하여 하나의 섬을 탐색"""
        q = deque([start])
        visited[start[1]][start[0]] = True  # 방문 처리

        while q:
            curx, cury = q.popleft()
            for i in range(8):
                nx, ny = curx + dx[i], cury + dy[i]

                if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and grid[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))

    island_count = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 1 and not visited[y][x]:
                island_count += 1
                bfs((x, y))

    return island_count

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    island_map = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    print(count_island(w, h, island_map))