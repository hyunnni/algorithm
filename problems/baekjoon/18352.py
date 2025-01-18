import sys
from collections import deque

# 입력 처리
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[]for _ in range (n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# BFS 
def bfs(start):
    distances = [-1]*(n+1)  # 모든 도시에 대한 거리 초기화 (-1: 미방문)
    queue = deque([start])
    distances[start] = 0    # 시작 도시의 거리는 0
    
    while queue:
        cur = queue.popleft()

        for neighbor in graph[cur]:
            if distances[neighbor] == -1:   # 미방문 도시
                distances[neighbor] = distances[cur] + 1
                queue.append(neighbor)
    
    return distances

# 시작 도시에서 모든 도시까지의 최단거리 계산
distances = bfs(x)

# 거리 k에 해당하는 도시 출력
result = [i for i in range(1, n+1) if distances[i] == k]

if result:
    print('\n'.join(map(str,result)))
else:
    print(-1)