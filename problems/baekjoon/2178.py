import sys
from collections import deque

# 미로 크기 입력
height, width = map(int,sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(height)]

# BFS
def bfs(start_x, start_y):
    # 큐 초기화
    queue = deque([(start_y, start_x,1)]) # 큐에 튜플 형태로 저장
    # 방문 배열 초기화
    visited = [[False] * width for _ in range(height)]
    visited[start_y][start_x] = True

    # 이동 방향(상하좌우)
    dx = [-1,1,0,0]   
    dy = [0,0,-1,1]

    while queue:
        cury, curx, dist = queue.popleft()
        
        # 도착지점에 도달하면 거리 반환
        if cury == height - 1 and curx == width - 1:
            return dist

        # 상하좌우 탐색
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            
            # 범위 확인, 방문하지 않은 칸 처리
            if 0 <= nx < width and 0 <= ny < height:
                if maze[ny][nx] == 1 and visited[ny][nx] == False:
                    queue.append([ny, nx, dist+1])
                    visited[ny][nx] = True

# 실행 및 결과 출력
result = bfs(0, 0)
print(result)