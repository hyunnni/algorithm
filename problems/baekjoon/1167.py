import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

# 그래프 입력
for _ in range(V):
    temp = list(map(int, input().split()))
    node = temp[0]
    idx = 1
    while idx < len(temp) - 1:
        graph[node].append((temp[idx], temp[idx + 1]))
        idx += 2

def bfs(start):
    q = deque([(start, 0)])
    visited = [-1] * (V + 1)    # 미방문 : -1, 방문 : (거리)
    visited[start] = 0
    farthest_node, max_dist = start, 0

    while q:
        cur, dist = q.popleft()
        for next_node, weight in graph[cur]:
            if visited[next_node] == -1:    # 방문하지 않은 노드
                visited[next_node] = dist + weight
                q.append((next_node, visited[next_node]))
                if visited[next_node] > max_dist:   # 가장 먼 노드
                    max_dist = visited[next_node]
                    farthest_node = next_node

    return farthest_node, max_dist

# 1. 임의의 노드에서 가장 먼 노드 찾기
A, _ = bfs(1)
# 2. 1에서 가장 먼 노드 찾기 ( == 트리 지름)
B, diameter = bfs(A)

print(diameter)