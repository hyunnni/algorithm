import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search_location():
    global s_loc, w_loc
    s_loc = None    # 고슴도치 위치
    w_loc = []      # 물 위치 리스트

    for y in range(r):
        for x in range(c):
            if grid[y][x] == 'S':
                s_loc = (x,y)
            if grid[y][x] == '*':
                w_loc.append((x,y))

def bfs():
    global grid
    sq = deque()    # 고슴도치 이동 큐
    wq = deque()    # 물 확장 큐
    
    visited = [[False] * c for _ in range(r)]   # 방문 여부

    # 큐 초기화
    sx, sy = s_loc
    sq.append((sx, sy, 0)) # (x, y, 시간)
    visited[sy][sx] = True

    for wx, wy in w_loc:
        wq.append((wx, wy)) # 물 위치 큐에 추가

    while sq:
        # 1. 물 확장 (BFS 1)
        for _ in range(len(wq)):    # 현재 있는 물 확장
            wx, wy = wq.popleft()
            for i in range(4):
                nx, ny = wx + dx[i], wy + dy[i]
                if 0 <= nx < c and 0 <= ny < r and grid[ny][nx] == '.':
                    grid[ny][nx] = '*'  # 물 확장
                    wq.append((nx, ny))

        # 2. 고슴도치 이동 (BFS 2)
        for _ in range(len(sq)):    # 현재 고슴도치 이동
            cx, cy, time = sq.popleft()

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0 <= nx < c and  0 <= ny < r:
                    if grid[ny][nx] == 'D': # 비버 굴 도착
                        return time + 1
                    
                    if grid[ny][nx] == '.' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        sq.append((nx, ny, time + 1))
        
    return "KAKTUS"

search_location()
print(bfs())