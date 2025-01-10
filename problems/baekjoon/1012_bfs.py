import sys
from collections import deque

# bfs
def bfs (field_map, x, y, visited):
    queue = deque([(x, y)]) # 큐 생성, 초기값 넣기
    visited[y][x] = True    # 방문처리

    # 이동 방향
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:    # 큐에 값이 사라질 때까지
        curx, cury = queue.popleft()

        # 상하좌우 탐색 
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            # 맵 크기 유효 확인 
            if 0 <= nx < len(field_map[0]) and 0 <= ny < len(field_map):
                # 배추 유무, 방문여부 확인
                if field_map[ny][nx] == 1 and not visited:
                    # 큐에 추가 및 방문처리
                    queue.append((nx, ny))
                    visited[ny][nx] = True

# 테스트 케이스 입력
test_cases = int(sys.stdin.readline())

for _ in range(test_cases):
    width, height, num_cabbages = map(int,sys.stdin.readline().split())
    field_map = [[0] * width for _ in range(height)]  # 배추밭 배열 초기화
    visited = [[False] * width for _ in range(height)]   # 방문 배열 초기화

    for _ in range(num_cabbages):
        col, row = (map(int,sys.stdin.readline().split()))
        field_map[row][col] = 1 # 배추 위치 표시

    worm_count = 0

    for y in range(height):
        for x in range(width):
            # 새로운 군집 발견
            if field_map[y][x] == 1 and not visited:
                bfs(field_map, x, y, visited)
                worm_count += 1 # 지렁이 수 추가
    
    # 결과 출력
    print(worm_count)   