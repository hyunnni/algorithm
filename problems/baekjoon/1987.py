import sys
from collections import deque

def count_dist():
    r, c = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(r)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs():
        max_dist = 1    
        q = deque([(0, 0, 1, {grid[0][0]})])    # (x, y, 이동 거리, 지나온 알파벳 set)
        
        while q : 
            cx , cy, dist, path = q.popleft()
            max_dist = max(max_dist, dist)
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0 <= nx < c and 0 <= ny < r and grid[ny][nx] not in path:
                    q.append((nx, ny, dist + 1, path | {grid[ny][nx]})) # 새로운 경로 저장
                    
        return max_dist
    
    return bfs()

print(count_dist())