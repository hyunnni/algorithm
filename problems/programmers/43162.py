from collections import deque

def solution(n, computers):
    visited = [False]*n # 방문 배열 초기화
    answer = 0  # 네트워크 개수

    # BFS 함수
    def bfs(com):
        queue = deque([com])
        visited[com] = True # 시작 노드 방문 처리

        while queue:
            cur_com = queue.popleft()
            
            # 현재 컴퓨터와 연결된 컴퓨터 탐색
            for i in range(n):
                if computers[cur_com][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    # 모든 컴퓨터 순회하며 네트워크 탐색
    for i in range(n):
        if not visited[i]:  # 방문하지 않은 컴퓨터 발견
            bfs(i)  # 해당 컴퓨터 기준으로 네트워크 탐색
            answer+=1   # 새로운 네트워크 발견
    
    return answer