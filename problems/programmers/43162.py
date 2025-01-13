from collections import deque

def solution(n, computers):
    visited = [False]*n
    answer = 0

    # BFS
    def bfs(com):
        queue = deque([com])
        visited[com] = True

        while queue:
            cur_com = queue.popleft()

            for i in range(n):
                if computers[cur_com][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer+=1
    
    return answer