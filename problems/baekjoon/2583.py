import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
grid = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
area_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 직사각형 칠하기
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sx, ex = x1, x2 - 1
    sy, ey = M - y2, M - y1 - 1 # 좌표 변환

    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            grid[y][x] = 1  # 직사각형 표시

# 영역 넓이 구하기(BFS)
def count_area(sx, sy):
    area = 1
    visited[sy][sx] = True
    q = deque([(sx, sy)])
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[ny][nx] and grid[ny][nx] == 0:
                    visited[ny][nx] = True
                    area += 1
                    q.append((nx, ny))
        
    return area

# BFS 실행
for y in range(M):
    for x in range(N):
        if grid[y][x] == 0 and not visited[y][x]:   # 새 영역 발견
            area_list.append(count_area(x, y))  # 넓이 계산

# 출력
area_list.sort()
print(len(area_list))
print(*area_list)