import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    temp = list(map(int, input().split()))
    node = temp[0]
    idx = 1
    while idx < len(temp) - 1:
        graph[node].append((temp[idx], temp[idx + 1]))
        idx += 2

def bfs(start):
    q = deque([(start, 0)])
    visited = [-1] * (V + 1)
    visited[start] = 0
    farthest_node, max_dist = start, 0

    while q:
        cur, dist = q.popleft()
        for next_node, weight in graph[cur]:
            if visited[next_node] == -1:
                visited[next_node] = dist + weight
                q.append((next_node, visited[next_node]))
                if visited[next_node] > max_dist:
                    max_dist = visited[next_node]
                    farthest_node = next_node

    return farthest_node, max_dist

A, _ = bfs(1)
B, diameter = bfs(A)

print(diameter)