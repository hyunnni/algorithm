import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    # ✅ dist 배열을 3차원으로 변경하여 벽 부순 여부를 따로 저장
    dist = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    dist[0][0][0] = 1  # 시작 위치 설정 (벽을 부수지 않은 상태)

    q = deque([(0, 0, 0)])  # ✅ (x, y, 벽 부순 여부) 추가

    while q:
        cx, cy, broken = q.popleft()

        # ✅ 목표 지점 도착하면 거리 반환
        if cx == M - 1 and cy == N - 1:
            return dist[cy][cx][broken]

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                # 1️⃣ 벽이 아닌 경우 → 그냥 이동
                if grid[ny][nx] == 0 and dist[ny][nx][broken] == 0:
                    dist[ny][nx][broken] = dist[cy][cx][broken] + 1
                    q.append((nx, ny, broken))

                # 2️⃣ 벽인 경우 → 벽을 한 번만 부술 수 있음
                elif grid[ny][nx] == 1 and broken == 0:  # ✅ 아직 벽을 부수지 않은 상태라면
                    dist[ny][nx][1] = dist[cy][cx][broken] + 1  # ✅ 벽을 부순 상태로 이동
                    q.append((nx, ny, 1))

    return -1  # ❌ 최단 경로가 없는 경우

print(bfs())