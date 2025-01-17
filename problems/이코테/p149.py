import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    ice_map = []
    for _ in range(n):
        ice_map.append(list(map(int, sys.stdin.readline().strip())))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = 0

    def dfs(x, y):
        ice_map[y][x] = 1  # 현재 위치 방문 처리

        for i in range(4):  # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and ice_map[ny][nx] == 0:
                dfs(nx, ny)

    for i in range(n):  # 모든 위치 탐색
        for j in range(m):
            if ice_map[i][j] == 0:  # 방문하지 않은 구멍(0)을 발견하면 DFS 호출
                dfs(j, i)
                result += 1  # 아이스크림 개수 증가

    return result

print(solve())