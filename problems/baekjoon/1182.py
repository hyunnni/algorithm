import sys

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

count = 0

def backtrack(idx, total):
    global count

    if idx >= N:
        return
    
    total += numbers[idx]
    if total == S:
        count += 1

    backtrack(idx + 1, total)
    backtrack(idx + 1, total - numbers[idx])

backtrack(0,0)
print(count)
    
