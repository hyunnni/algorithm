import sys

map_list = []
result_list = []
n = int(input())
for _ in range(n):
    map_list.append(list(map(int, sys.stdin.readline().strip())))

def dfs(x, y):
    map_list[y][x] = 0
    cnt = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0<= ny < n and map_list[ny][nx] == 1:
            cnt += dfs(nx, ny)
    
    return cnt

for y in range(n):
    for x in range(n):
        if map_list[y][x] == 1:
            result_list.append(dfs(x,y))
            

result_list.sort()
print(len(result_list))
for result in result_list:
    print(result)

