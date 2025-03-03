import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
map_list = [list(map(int, sys.stdin.readline().strip()))for _ in range(n)]

def bfs():
    # 방문 배열
    visited = [[[False]*(k + 1) for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 1, 0)]) # x, y, dist, break_count
    visited[0][0][0] = True # 시작점 방문 처리

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        curx, cury, dist, break_count = queue.popleft()

        # 도착점 도달 경우
        if curx == m - 1 and cury == n - 1:
            return dist

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            # 유효 좌표 확인
            if 0 <= nx < m and 0 <= ny < n:
                # 벽이 아닌 경우
                if map_list[ny][nx] == 0 and not visited[ny][nx][break_count]:
                    visited[ny][nx][break_count] = True
                    queue.append((nx, ny, dist + 1, break_count))
                
                # 벽인 경우
                elif map_list[ny][nx] == 1 and break_count < k and not visited[ny][nx][break_count + 1] :
                    visited[ny][nx][break_count + 1] = True
                    queue.append((nx, ny, dist + 1, break_count +1))
    
    # 도달 불가 경우
    return -1

print(bfs())