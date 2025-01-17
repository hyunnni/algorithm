import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    ice_map= []
    for i in range(n):
        ice_map.append(list(map(int,sys.stdin.readline().strip())))

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    result = 0
        
    def dfs(x, y):
        ice_map[y][x] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and ice_map[ny][nx] == 0:
                dfs(nx,ny)
                
    for i in range(n):
        for j in range(m):
            if ice_map[i][j] == 0:
                dfs(j,i)
                result += 1
    
    return result

print(solve())