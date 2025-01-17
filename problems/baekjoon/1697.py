from collections import deque

# 입력
start, end = map(int, input().split())

# bfs 정의
def bfs():
    queue = deque([(start,0)])  
    visited = [False] * 100001  # 방문 여부 배열
    visited[start] = True   # 시작 위치 방문 처리

    while queue:
        cur, time = queue.popleft()
        
        # 동생 위치에 도달하면 경과 시간 반환
        if cur == end:
            return time

        # 이동 가능한 위치 탐색
        for next_pos in (cur -1 , cur + 1, cur * 2):
            if 0<= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True    # 방문 처리
                queue.append((next_pos, time + 1))  # 큐에 추가
        
print(bfs())