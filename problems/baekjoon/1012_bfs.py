import sys
from collections import deque

def bfs (fieldMap, x, y, visited):
    queue = deque([(x, y)])
    visited[y][x] = True

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        curx, cury = queue.popleft()

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0 <= nx < len(fieldMap[0]) and 0 <= ny < len(fieldMap):
                if fieldMap[ny][nx] == 1 and visited[ny][nx] == False:
                    queue.append((nx, ny))
                    visited[ny][nx] = True

# 테스트 케이스 입력
testCase = int(sys.stdin.readline())

for _ in range(testCase):
    width, height, num_cabbages = map(int,sys.stdin.readline().split())
    fieldMap = [([0]*width)for _ in range(height)]
    visited = [([False]*width)for _ in range(height)]

    for _ in range(num_cabbages):
        col, row = (map(int,sys.stdin.readline().split()))
        fieldMap[row][col] = 1 

    worm_count = 0

    for y in range(height):
        for x in range(width):
            if fieldMap[y][x] == 1 and visited[y][x] == False:
                bfs(fieldMap, x, y, visited)
                worm_count += 1
    
    print(worm_count)   