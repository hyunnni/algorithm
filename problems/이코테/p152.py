import sys
from collections import deque

def solution():
    n, m = map(int, sys.stdin.readline().split())
    monster_map = []
    for _ in range(n):
        monster_map.append(list(map(int, sys.stdin.readline().strip())))

    def bfs():
        queue = deque([(0, 0)]) # 시작 위치
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        while queue:
            curx, cury = queue.popleft()

            # 목적지 도착 시 거리 반환
            if curx == m - 1 and cury == n - 1:
                return monster_map[cury][curx]

            # 상하좌우 탐색
            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]

                # 유효 범위, 괴물 여부 확인
                if 0 <= nx < m and 0<= ny < m and monster_map[ny][nx] == 1:
                    queue.append((nx, ny))
                    # 이동 거리 갱신 및 방문 처리
                    monster_map[ny][nx] = monster_map[cury][curx] + 1
        
        return -1   # 도달 불가능한 경우 (문제 조건상 발생하지 않는다)

    # 결과 출력
    print(bfs())

solution()