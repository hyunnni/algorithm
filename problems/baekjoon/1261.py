import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())
map_list = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * m  for _ in range(n)]

def bfs():

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([(0,0,0)]) # x, y, 뚫 개수
    visited[0][0] = True

    while queue:
        cur_x, cur_y, break_count = queue.popleft()
        if cur_x == m-1 and cur_y == n-1:
            return break_count
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
        
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    
                    if map_list[ny][nx] == 0:
                        queue.appendleft((nx, ny, break_count))

                    elif map_list[ny][nx] == 1:
                        queue.append((nx,ny,break_count+1))

    return -1

print(bfs())