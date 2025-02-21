from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

flist = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    flist[x].append(y)  
    flist[y].append(x)  # 양방향

def bfs(start, target):
    q = deque([(start, 0)])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        cur, count = q.popleft()

        if cur == target:   # 목표 노드
            return count

        for next_person in flist[cur]:
            if not visited[next_person]:
                visited[next_person] = True
                q.append((next_person, count + 1))

    return -1   # 계산 불가가

print(bfs(a, b))