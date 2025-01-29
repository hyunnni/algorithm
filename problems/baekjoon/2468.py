import sys
from collections import deque

def bfs(map, rain, startx, starty):
    queue = deque([(startx, starty)])
    visited[starty][startx] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        curx, cury = queue.popleft()
        for dx, dy in directions:
            nx, ny = curx + dx, cury + dy

            # 범위, 방문 여부, 물에 잠긴 여부 확인
            if 0 <= nx < n and 0 <= ny < n and map[ny][nx] > rain and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))

# 입력 처리
n = int(sys.stdin.readline())
height_map = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
max_height = max(map(max, height_map))  # 최대 높이

""" 비가 아예 안 올 경우를 대비해 초기값 1로 설정"""
answer = 1  

# 각 강수량마다 BFS 수행
for rain in range(1, max_height):   # 비 높이는 1부터 max_height - 1까지
    visited = [[False] * n for _ in range (n)]
    cnt  = 0    # 안전 영역 개수 카운트

    for y in range(n):
        for x in range(n):
            if not visited[y][x] and height_map[y][x] > rain:
                bfs(height_map, rain, x, y)
                cnt += 1    # 새로운 안전 영역 발견
    
    # 더 이상 안전 영역이 없으면 중단 
    if cnt == 0:
        break

    answer = max(answer, cnt)

print(answer)