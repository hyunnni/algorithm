from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs():
        queue = deque([(0,0)])
        
        while queue:
            curx, cury = queue.popleft()
            
            if curx == cols - 1 and cury == rows - 1 :
                return maps[cury][curx]
            
            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]
                
                if 0<= nx < cols and 0 <= ny < rows and maps[ny][nx] == 1:
                    maps[ny][nx] = maps[cury][curx] + 1
                    queue.append((nx, ny))
        
        return -1
    
    return bfs()