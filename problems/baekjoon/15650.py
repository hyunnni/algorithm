import sys

N, M = map(int, sys.stdin.readline().split())
result = []

def backtrack(start, depth):
    if depth == M:  # M개 선택하면 출력
        print(*result)
        return

    for i in range(start, N + 1):   # start부터 탐색 (중복X)
        result.append(i)
        backtrack(i + 1, depth + 1) # (오름차순)
        result.pop()    # 원상복구

backtrack(1, 0)