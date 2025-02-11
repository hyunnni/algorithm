import sys
from collections import deque

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    building = [list(sys.stdin.readline().strip()) for _ in range(h)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs():
        fireq = deque([])
        sq = deque([])

        for y in range(h):
            for x in range(w):
                if building[y][x] == '@':
                    sx, sy = x, y
                    sq.append((sx, sy, 0))
                elif building[y][x] == '*':
                    fireq.append((x, y, 0))

        while sq:
            for _ in range(len(fireq)):
                fx, fy, time = fireq.popleft()
                for i in range(4):
                    nfx, nfy = fx + dx[i], fy + dy[i]
                    if 0 <= nfx < w and 0 <= nfy < h and building[nfy][nfx] == '.':
                        building[nfy][nfx] = '*'
                        fireq.append((nfx, nfy, time + 1))

            for _ in range(len(sq)):
                sx, sy, time = sq.popleft()

                if sx == 0 or sx == w-1 or sy == 0 or sy == h-1:
                    print(time + 1)
                    return

                for i in range(4):
                    nsx, nsy = sx + dx[i], sy + dy[i]
                    if 0 <= nsx < w and 0 <= nsy < h and building[nsy][nsx] == '.':
                        building[nsy][nsx] = '@'
                        sq.append((nsx, nsy, time + 1))

        print("IMPOSSIBLE")

    bfs()