from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = 0
    max_dist = 0
    
    while queue:
        x, y = queue.popleft()
        
        max_dist = max(max_dist, visited[x][y])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
    return max_dist

result = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
