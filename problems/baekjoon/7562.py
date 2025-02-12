import sys
from collections import deque

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def get_min_knight_moves(start_x: int, start_y: int, end_x: int, end_y: int, board_size: int) -> int:
    if start_x == end_x and start_y == end_y:
        return 0

    visited = [[False] * board_size for _ in range(board_size)]
    visited[start_y][start_x] = True
    q = deque([(start_x, start_y, 0)])

    while q:
        curr_x, curr_y, moves = q.popleft()
        
        for i in range(8):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            
            if 0 <= next_x < board_size and 0 <= next_y < board_size and not visited[next_y][next_x]:
                if next_x == end_x and next_y == end_y:
                    return moves + 1
                
                visited[next_y][next_x] = True
                q.append((next_x, next_y, moves + 1))

    return -1

T = int(sys.stdin.readline().strip())
for _ in range(T):
    I = int(sys.stdin.readline().strip())
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())

    print(get_min_knight_moves(sx, sy, ex, ey, I))