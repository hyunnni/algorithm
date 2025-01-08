import sys
sys.setrecursionlimit(10**6)

testCase = int(sys.stdin.readline())

def dfs(fieldMap, x, y):
    fieldMap[y][x] = 2

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < len(fieldMap[0]) and 0 <= ny < len(fieldMap):
            if fieldMap[ny][nx] == 1:
                dfs(fieldMap, nx, ny)


for i in range(testCase):
    m, n, k = map(int,sys.stdin.readline().split())
    fieldMap = [([0]*m)for _ in range(n)]

    for _ in range(k):
        a, b = (map(int,sys.stdin.readline().split()))
        fieldMap[b][a] = 1

    worm_cnt = 0

    for y in range(n):
        for x in range(m):
            if fieldMap[y][x] == 1:
                dfs(fieldMap, x, y)
                worm_cnt += 1            
        
    print(worm_cnt)