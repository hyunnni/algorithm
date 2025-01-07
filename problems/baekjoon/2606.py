import sys

# 입력 처리
com = int(sys.stdin.readline())
connections = int(sys.stdin.readline())

# 그래프 초기화
graph = [[]for _ in range(com+1)]

# 그래프 구성
for _ in range(connections):
    a,b = map(int, sys.stdin.readline().split)
    graph[a].append(b)
    graph[b].append(a)

# 방분 배열 초기화 
visited = [False]*(com+1)

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# DFS 실행    
dfs(graph,1, visited)

# 1번 컴퓨터 제외한 감염된 컴퓨터 수 출력
print(visited.count(True)-1)