import sys
from collections import deque

# 입력 처리
m,n = map(int, sys.stdin.readline().split())
map_list = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

# 방문 배열
visited = [[False] * m  for _ in range(n)]

# BFS 함수 정의
def bfs():

    # 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # BFS 큐 초기화 (x, y, 벽을 부순 횟수)
    queue = deque([(0,0,0)])    # 시작점(0,0)에서 출발
    visited[0][0] = True    # 시작점 방문 처리

    while queue:
        cur_x, cur_y, break_count = queue.popleft()

        # 도착 지점에 도달한 경우
        if cur_x == m-1 and cur_y == n-1:
            return break_count  # 부순 횟수 반환
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
        
            # 좌표 유효성 확인 (범위내)
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx]: # 방문하지 않은 경우
                    visited[ny][nx] = True  # 방문 처리
                    
                    # 벽이 아닌 경우
                    if map_list[ny][nx] == 0:
                        # 벽 부수지 않고 이동
                        queue.appendleft((nx, ny, break_count)) # 부순 횟수가 적어지기 때문에 우선적 탐색하기 위해 appendleft()

                    # 벽인 경우 (부수고 이동)
                    elif map_list[ny][nx] == 1:
                        queue.append((nx,ny,break_count+1))

    return -1

print(bfs())