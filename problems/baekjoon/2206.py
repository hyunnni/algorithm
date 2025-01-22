import sys
from collections import deque

# 입력 처리
n, m = map(int, sys.stdin.readline().split())
map_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# BFS 함수 정의
def bfs():
    # 방문 배열: visited[y][x][0] -> 벽을 뚫지 않은 상태, visited[y][x][1] -> 벽을 뚫은 상태
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 1, 0)])  # (x, y, 거리, 벽을 뚫었는지 여부)
    visited[0][0][0] = True  # 시작 지점 방문 처리 (벽을 뚫지 않은 상태)

    # 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        curx, cury, dist, wall_break = queue.popleft()

        # 도착지점에 도달한 경우 거리 반환
        if curx == m - 1 and cury == n - 1:
            return dist

        # 상하좌우 이동
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            # 유효한 좌표인지 확인
            if 0 <= nx < m and 0 <= ny < n:
                # 벽이 아닌 경우
                if map_list[ny][nx] == 0 and not visited[ny][nx][wall_break]:
                    visited[ny][nx][wall_break] = True
                    queue.append((nx, ny, dist + 1, wall_break))

                # 벽인 경우, 벽을 뚫을 수 있다면
                elif map_list[ny][nx] == 1 and wall_break == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    queue.append((nx, ny, dist + 1, 1))

    return -1  # 도착할 수 없는 경우 

# 결과 출력
print(bfs())