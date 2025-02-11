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
        time = 0

        # 초기 위치 탐색        
        for y in range(h):
            for x in range(w):
                if building[y][x] == '@':
                    sx, sy = x, y
                    sq.append((sx, sy))  # 사람 위치 추가
                elif building[y][x] == '*':
                    fireq.append((x, y)) # 불 위치 추가

        # 불, 사람 번갈아가며 BFS 실행 ( 불 확산 -> 사람 이동)
        while sq:   # 사람(`sq`)이 없으면 더 진행할 필요 없음
            # `while sq`인 이유 : 사람이 모두 탈출하지 못하고 `sq`가 먼저 비었을 경우 `fireq`가 남아 있어서 무한 루프가 될 수 있음
            time += 1
            # 🔥 불 먼저 확산
            for _ in range(len(fireq)):
                fx, fy = fireq.popleft()
                for i in range(4):
                    nfx, nfy = fx + dx[i], fy + dy[i]
                    if 0 <= nfx < w and 0 <= nfy < h and building[nfy][nfx] == '.':
                        building[nfy][nfx] = '*'    # 불 번짐 표시
                        fireq.append((nfx, nfy))

            # 🕺 상근이 이동
            for _ in range(len(sq)):
                sx, sy = sq.popleft()

                # 탈출 조건 : 가장자리 도달
                if sx == 0 or sx == w-1 or sy == 0 or sy == h-1:
                    print(time)
                    return

                for i in range(4):
                    nsx, nsy = sx + dx[i], sy + dy[i]
                    if 0 <= nsx < w and 0 <= nsy < h and building[nsy][nsx] == '.':
                        building[nsy][nsx] = '@'    # 사람 이동 표시 (불 구분 위해)
                        sq.append((nsx, nsy))

        print("IMPOSSIBLE") # 모든 BFS가 끝날 때까지 탈출하지 못한 경우

    bfs()