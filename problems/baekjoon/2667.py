import sys

# 입력 처리
map_list = []
result_list = []
n = int(input())
for _ in range(n):
    map_list.append(list(map(int, sys.stdin.readline().strip())))

# DFS 함수 정의
def dfs(x, y):
    map_list[y][x] = 0  # 방문 처리
    cnt = 1 # 처리 집 카운트 

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0<= ny < n and map_list[ny][nx] == 1:
            cnt += dfs(nx, ny)  # 인접한 집 카운트 누적
    
    return cnt

# 모든 칸 순회하며 DFS 호출
for y in range(n):
    for x in range(n):
        if map_list[y][x] == 1: # 방문하지 않은 단지 발견
            result_list.append(dfs(x,y))    # 단지에 속하는 집의 수 추가 
            
# 결과 출력 
result_list.sort()
print(len(result_list)) # 총 단지 수 출력
for result in result_list:
    print(result)   # 각 단지의 크기 출력 