import sys
from collections import deque

# 입력
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

# 무방향그래프 -> 양방향 간선 처리
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부 체크 배열
visited = [False] * (n + 1)

# BFS 함수
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 연결 요소 개수 계산
connected_component = 0
for i in range(1, n + 1):
    if not visited[i]:  # 아직 방문하지 않은 노드라면
        connected_component += 1
        bfs(i)  # BFS 호출 : 연결된 모든 노드 방문

print(connected_component)