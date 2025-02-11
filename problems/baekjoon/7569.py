import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split()))for _ in range(N)]for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    q = deque([])
    max_day = 1

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    q.append((x, y, z))
    
    while q:
        cx, cy, cz = q.popleft()
        for i in range(6):
            nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]
            
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[cz][cy][cx] + 1
                max_day = max(max_day, box[nz][ny][nx])
                q.append((nx, ny, nz))
        
    return max_day

def count_days():
    # 처음부터 모든 토마토가 익어있는 경우
    if not any(0 in row for layer in box for row in layer):
        print(0)
        return
        
    max_day = bfs()

    # 토마토가 모두 익지 못하는 경우
    if any(0 in row for layer in box for row in layer):
        print(-1)
        return 
    
    print(max_day - 1)

count_days()