import sys
from collections import deque

def solution():
    n, m = map(int, sys.stdin.readline().split())
    monster_map = []
    for _ in range(n):
        monster_map.append(list(map(int, sys.stdin.readline().strip())))

    def bfs():
        queue = deque([(0, 0)])
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        while queue:
            curx, cury = queue.popleft()

            if curx == m - 1 and cury == n - 1:
                return monster_map[cury][curx]

            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]

                if 0 <= nx < m and 0<= ny < m and monster_map[ny][nx] == 1:
                    queue.append((nx, ny))
                    monster_map[ny][nx] = monster_map[cury][curx] + 1
        
        return -1

    print(bfs())

solution()