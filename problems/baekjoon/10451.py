import sys
from collections import deque

def count_permutation(permutation):
    cycle_cnt = 0
    visited = [False]*(per_size)

    def bfs(start):
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            neighbor = graph[node]-1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    for p in range (len(permutation)):
        if not visited[p]:
            bfs(p)
            cycle_cnt += 1

    print(cycle_cnt)

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    per_size = int(sys.stdin.readline())
    graph = list(map(int, sys.stdin.readline().split()))
    count_permutation(graph)