from collections import deque

def solution(n, computers):
    graph = [[]*n for _ in range(n)]
    visited = [False]*n
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                bfs(n,computers,i,visited)
                answer+=1
    
    return answer

def bfs(n,computers, com, visited):
    queue = deque([com])
    visited[com] = True
    
    while queue:
        cur_com = queue.popleft()
        print(cur_com, end='')
        
        #해당 요소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(n):
            if i != cur_com:
                if computers[cur_com][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True