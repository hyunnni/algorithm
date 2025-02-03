import sys

def count_dist():
    r, c = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(r)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = set()  # 방문한 알파벳을 저장하는 set
    max_dist = 0

    def dfs(x, y, dist):
        nonlocal max_dist
        max_dist = max(max_dist, dist)
        
        visited.add(grid[y][x])  # 현재 알파벳 방문 기록

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < c and 0 <= ny < r and grid[ny][nx] not in visited:
                dfs(nx, ny, dist + 1)

        visited.remove(grid[y][x])  # 백트래킹

    dfs(0, 0, 1)
    return max_dist

print(count_dist())