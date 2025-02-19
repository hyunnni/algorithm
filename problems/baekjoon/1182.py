import sys

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

count = 0

def backtrack(idx, total):
    global count

    if idx >= N:    #모든 원소 확인한 경우
        return
    
    # 현재 원소 선택한 경우
    total += numbers[idx]
    if total == S:
        count += 1  # 조건 만족하는 경우 카운트 ++

    backtrack(idx + 1, total)   # 다음 원소 탐색 (현재 원소 선택한 경우)
    backtrack(idx + 1, total - numbers[idx])    # 원상복구

backtrack(0,0)
print(count)