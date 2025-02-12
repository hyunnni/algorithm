import sys
from collections import deque

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def count_move(sx, sy, ex, ey, I):
    if sx == ex and sy == ey:
        return 0

    visited = [[False] * I for _ in range(I)]
    visited[sy][sx] = True
    q = deque([(sx, sy, 0)])

    while q:
        cx, cy, move = q.popleft()
        
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < I and 0 <= ny < I and not visited[ny][nx]:
                if nx == ex and ny == ey:
                    return move + 1
                
                visited[ny][nx] = True
                q.append((nx, ny, move + 1))

    return -1

T = int(sys.stdin.readline().strip())
for _ in range(T):
    I = int(sys.stdin.readline().strip())
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())

    print(count_move(sx, sy, ex, ey, I))