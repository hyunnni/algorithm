import sys

N, M = map(int, sys.stdin.readline().split())
result = []

def backtrack(start, depth):
    if depth == M:
        print(*result)
        return

    for i in range(start, N + 1):
        result.append(i)
        backtrack(i + 1, depth + 1)
        result.pop()

backtrack(1, 0)