import sys
sys.setrecursionlimit(10**6) # 재귀 제한 늘림

# DFS 정의
def dfs(farm, x, y):
    farm[y][x] = 2  # 현재 위치 방문 처리

    # 상하좌우 이동 방향 정의
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # 상하좌우로 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 이동하려는 좌표의 유효 범위 확인
        if 0 <= nx < len(farm[0]) and 0 <= ny < len(farm):
            # 방문하지 않은 배추가 있으면 DFS 재귀 호출
            if farm[ny][nx] == 1:
                dfs(farm, nx, ny)

# 테스트 케이스 입력
testCase = int(sys.stdin.readline())

for _ in range(testCase):
    # 배추밭의 가로, 세로 크기와 배추 개수 입력
    width, height, num_cabbages = map(int,sys.stdin.readline().split())
    # 배추밭 0으로 초기화 (2D 배열)
    fieldMap = [([0]*width)for _ in range(height)]

    # 배추 위치 입력
    for _ in range(num_cabbages):
        col, row = (map(int,sys.stdin.readline().split()))
        fieldMap[row][col] = 1  # 배추 심어진 위치를 1로

    # 배추흰지렁이 수 계산
    worm_count = 0

    # 배추밭을 순회하며 DFS 실행
    for y in range(height):
        for x in range(width):
            # 배추가 있고 방문하지 않은 새로운 군집 발견
            if fieldMap[y][x] == 1:
                dfs(fieldMap, x, y)
                worm_count += 1   # 군집이 발견될 때마다 지렁이 수 증가
    
    # 결과 출력
    print(worm_count)