# BFS : Breadth-First Search

<br>

## BFS란?

> 너비 우선 탐색으로, 루트 노드를 시작으로 가까운 노드부터 탐색하는 방법

![image](https://github.com/user-attachments/assets/09ff50a9-185e-48b0-9cb8-59a5dd35f10c)

<br>
<br>

## BFS의 동작 과정

1. 시작 정점으로 정해진 정점을 방문 (A)
2. 1에서 방문한 정점에 인접한 정점을 모두 방문 (B,C)
3. 2에서 방문한 정점에 인접한 정점 중 방문하지 않은 정점을 모두 방문 (D,E,F,G)
4. 3에서 방문한 정점에 인접한 정점 중 방문하지 않은 정점을 모두 방문 (H)
5. 4에서 방문한 정점 중 방문하지 않은 정점이 없어 더 이상 갈 곳이 없으므로 끝

<br>
<br>

## BFS의 구현 

![image](https://github.com/user-attachments/assets/95ddad56-ee3d-4ce8-85c0-ed2b046a0c48)

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

<br>
<br>


#### 구현 코드 (python)
```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])  # 큐(Queue) 구현 위해 deque 라이브러리 사용
    visited[start] = True   # 현재 노드를 방문 처리
    while queue:    # 큐가 빌 때까지 반복
        print("Current queue:", list(queue))  # 현재 큐의 상태 출력
        v = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력
        print(f"[Visited: {v}]")
        # 해당 원소와 연결되었지만 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 그래프를 2차원 리스트로 표현
graph = [
    [2, 1],
    [3, 2],
    [3],
    [4],
    [5, 1, 0],
    []
]

# 각 노드가 방문된 정보를 리스트로 표현
visited = [False] * 6

# BFS 함수 호출
bfs(graph, 0, visited)

```


#### OUTPUT
각 과정에서의 큐 상태와 방문 노드를 출력한 결과 
```
Current queue: [0]
[Visited: 0]
Current queue: [2, 1]
[Visited: 2]
Current queue: [1, 3]
[Visited: 1]
Current queue: [3]
[Visited: 3]
Current queue: [4]
[Visited: 4]
Current queue: [5]
[Visited: 5]
```