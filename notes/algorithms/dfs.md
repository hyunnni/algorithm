# DFS : Depth-First Search

<br>

## DFS란?

> 깊이 우선 탐색으로, 그래프에서 깊은 부분을 우선으로 탐색하는 방법

![image](https://github.com/user-attachments/assets/85a937fe-2428-4cdd-84fd-d322bde1d0ab)

<br>
<br>

## DFS의 동작 과정

1. 시작 노드를 방문한다
2. 방문하지 않은 인접 노드 중 가장 작은 노드를 스택에 넣고 방문한다
3. 스택의 최상단 노드에 방문하지 않은 노드를 스택에 넣고 방문한다
4. 스택의 최상단 노드에 방문하지 않은 인접 노드가 없을 경우 노드를 스택에서 꺼낸다
5. 남아 있는 노드에 방문하지 않은 인접 노드가 없어 노드를 차례대로 꺼내면 종료

<br>
<br>

## DFS의 구현

![image](https://github.com/user-attachments/assets/f32077d6-63cf-4067-8c81-c03fe636b6fb)

1. 탐색 시작 노드를 스택에 삽입하고 방문처리 한다
2. 1. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 쌓고 방문처리 한다
   2. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
3. 2의 과정을 더 이상 수행할 수없을 때까지 반복한다

<br>
<br>

### 구현 코드(python)

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
        
graph = [
    [1, 5],
    [2, 5],
    [3, 4],
    [],
    [3],
    [6],
    [1]
]

visited = [False]*7

dfs(graph, 0, visited)
```

### OUTPUT

````
0 1 2 3 4 5 6 
````

## 참고자료

- https://www.freecodecamp.org/news/the-value-of-graph-theory-within-sustainability/
- https://medium.com/@practicetracker4ever/depth-first-search-fd5900c20497
