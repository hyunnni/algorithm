import sys
from collections import deque
from copy import deepcopy

r, c = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

s_loc = None
w_loc = []

def search_location():
    global s_loc
    global w_loc
    for y in range(r):
        for x in range(c):
            if grid[y][x] == 'S':
                s_loc = (x,y)
            if grid[y][x] == '*':
                w_loc.append((x,y))

def bfs():
    global grid
    sq = deque()
    wq = deque()
    
    visited = [[False] * c for _ in range(r)]

    sx, sy = s_loc
    sq.append((sx, sy, 0))
    visited[sy][sx] = True

    for wx, wy in w_loc:
        wq.append((wx, wy))

    while sq:

        for _ in range(len(wq)):
            wx, wy = wq.popleft()
            for i in range(4):
                nx, ny = wx + dx[i], wy + dy[i]
                if 0 <= nx < c and 0 <= ny < r and grid[ny][nx] == '.':
                    grid[ny][nx] = '*'
                    wq.append((nx, ny))

        for _ in range(len(sq)):
            cx, cy, time = sq.popleft()

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0 <= nx < c and  0 <= ny < r:
                    if grid[ny][nx] == 'D':
                        return time + 1
                    
                    if grid[ny][nx] == '.' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        sq.append((nx, ny, time + 1))
        
    return "KAKTUS"

search_location()
print(bfs())