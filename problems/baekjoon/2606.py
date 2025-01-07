import sys

com = int(sys.stdin.readline())
match = int(sys.stdin.readline())

data = []
graph = [[]for _ in range(com+1)]

for _ in range(match):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in data:
    if i[1] not in graph[i[0]]:
        graph[i[0]].append(i[1])
    if i[0] not in graph[i[1]]:
        graph[i[1]].append(i[0])

    
visited = [False]*(com+1)

def dfs(graph, v, visited):
    visited[v] = True;
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
dfs(graph,1, visited)
print(visited.count(True)-1)