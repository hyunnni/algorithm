import sys
from collections import deque

# 순열 사이클 개수 계산 함수
def count_permutation(permutation):
    n = len(permutation)  # 순열의 크기
    visited = [False] * n  # 방문 여부 확인
    cycle_cnt = 0

    def bfs(start):
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            neighbor = permutation[node]  # 순열 값
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # 각 노드에서 BFS 실행
    for i in range(n):
        if not visited[i]:  # 방문하지 않았다면 사이클 시작
            bfs(i)
            cycle_cnt += 1

    return cycle_cnt

# 입력 처리
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    per_size = int(sys.stdin.readline())
    # 1-based index를 0-based index로 변환
    permutation = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    # 사이클 개수 계산 후 출력
    print(count_permutation(permutation))