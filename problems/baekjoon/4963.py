import sys
from collections import deque

def count_island(w, h, map):
    
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, -1, 0, 1, -1, 0, 1 ]

    def bfs(startx, starty):
        map[starty][startx] = -1
        q = deque([(startx, starty)])

        while q:
            curx, cury = q.popleft()
            
            for i in range(8):
                nx, ny = curx + dx[i] , cury + dy[i]

                if 0 <= nx < w and 0 <= ny < h:
                    if map[ny][nx] > 0:
                        map[ny][nx] = -1
                        q.append((nx, ny))
    
    island = 0

    for y in range(h):
        for x in range(w):
            if map[y][x] == 1:
                island += 1
                bfs(x, y)
                
    return island

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    else:
        map_list = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        print(count_island(w, h, map_list))
