from collections import deque

def solution(maps):
    rows = len(maps)    # 맵 세로 크기 
    cols = len(maps[0])     # 맵 가로 크기 
    
    # 이동 방향 
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    # BFS 함수 정의
    def bfs():
        queue = deque([(0,0)])  # 시작 위치 큐에 추가 
        
        while queue:
            curx, cury = queue.popleft()

            # 도착 지점에 도달한 경우 최단 거리 반환    
            if curx == cols - 1 and cury == rows - 1 :
                return maps[cury][curx]
            
            # 상하좌우 탐색 
            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]
                
                # 경계 조건 및 이동 가능 여부 확인
                if 0<= nx < cols and 0 <= ny < rows and maps[ny][nx] == 1:
                    maps[ny][nx] = maps[cury][curx] + 1 # 현재까지의 거리 +1 저장 
                    queue.append((nx, ny))  # 큐에 추가
        
        # BFS가 종료되었는데 도착지점에 도달하지 못한 경우 
        return -1
    
    return bfs()
