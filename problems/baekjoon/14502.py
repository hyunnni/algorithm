import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

# BFS: 바이러스 확산
def bfs(graph):
    # 바이러스 위치를 모두 큐에 넣고 BFS 탐색
    q = deque([(j, i) for i in range(n) for j in range(m) if graph[i][j] == 2]) # 초기 바이러스 위치 (graph 값이 2인 곳) 좌표 큐에 저장
    
    # 탐색 방향(상하좌우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 탐색 및 확산
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:  # 바이러스가 확산될 수 있는 위치면 (graph 값이 0이면)
                graph[ny][nx] = 2   # 확산 (값 = 2)
                q.append((nx, ny))
    
    # 안전 영역 개수 계산 및 최대값 갱신
    global answer
    count = sum([g.count(0) for g in graph])    # BFS 수행 후 0(안전구역) 개수 카운트
    answer = max(answer, count) # answer 변수에 최대값 갱신

# 입력 처리
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 벽 세울 수 있는 위치 리스트
wall_xy = [(x, y) for x in range(m) for y in range(n) if not graph[y][x]]

# 정답
answer = 0

# 벽 3개 세우는 모든 경우의 수 탐색
for c in combinations(wall_xy, 3): # wall_xy 중 3개 선택
    tmp_graph = deepcopy(graph) # graph 깊은 복사
    for x, y in c:
        tmp_graph[y][x] = 1 # 벽 세우기
    bfs(tmp_graph)  # BFS 실행 -> 안전구역 수 카운트

print(answer)