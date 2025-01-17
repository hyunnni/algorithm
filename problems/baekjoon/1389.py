from collections import deque
import sys

# 입력
n,m = map(int, sys.stdin.readline().split())
relationship = [[]for _ in range(n)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    relationship[a-1].append(b-1)
    relationship[b-1].append(a-1)

# BFS 정의
def bacon_game_bfs(p):
    bacon_list = [0] * n    # 각 사용자별 단계 정리
    visited = [False] * n   # 방문 여부
    queue = deque([(p, 0)]) # (현재 사용자, 현재 거리)
    visited[p] = True   # 방문 처리
    
    while queue:
        cur, dist = queue.popleft()
        for friend in relationship[cur]:
            if not visited[friend]:
                visited[friend] = True  
                bacon_list[friend] = dist + 1   # 거리 갱신
                queue.append((friend, dist + 1))

    return sum(bacon_list)

# main: 모든 사용자에 대해 BFS 실행
result_list = []
for p in range (n):
    result_list.append((p+1, bacon_game_bfs(p)))   # (user, bacon_result)

# 베이컨 값이 가장 작은 사용자 찾기
result = min(result_list, key=lambda x : (x[1], x[0]))  # 값 우선 기준 정렬, 값이 같으면 사용자 번호 기준 정렬
print(result[0])