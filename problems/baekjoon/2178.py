import sys
from collections import deque

height, width = map(int,sys.stdin.readline().split())
maze = []

for _ in range(height):
    maze.append(list(map(int,sys.stdin.readline().strip())))

def bfs(maze, start_x, start_y):
    queue = deque([[start_y, start_x,1]])
    visited = [[False] * width for _ in range(height)]
    visited[start_y][start_x] = True

    dx = [-1,1,0,0]   
    dy = [0,0,-1,1]

    while queue:
        cury, curx, dist = queue.popleft()
        
        if cury == height - 1 and curx == width - 1:
            print(dist)
            return

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0 <= nx < width and 0 <= ny < height:
                if maze[ny][nx] == 1 and visited[ny][nx] == False:
                    queue.append([ny, nx, dist+1])
                    visited[ny][nx] = True

bfs(maze, 0, 0)