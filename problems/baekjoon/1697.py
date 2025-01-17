from collections import deque
start, end = map(int, input().split())

def bfs():
    queue = deque([(start,0)])
    visited = [False] * 100001

    while queue:
        cur, time = queue.popleft()
        visited[cur] = True

        if cur == end:
            return time

        for next_pos in (cur -1 , cur + 1, cur * 2):
            if 0<= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))
        
    return 0

print(bfs())