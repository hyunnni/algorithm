import sys
from collections import deque

input = sys.stdin.readline

def get_input():
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    return m, n, box

def bfs(m, n, box):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    total_tomatoes = m * n
    empty_area = 0
    ripe_count = 0

    for y in range(n):
        for x in range(m):
            if box[y][x] == 1:
                q.append((x, y))
                ripe_count += 1
            elif box[y][x] == -1:
                empty_area += 1

    if ripe_count == total_tomatoes - empty_area:
        return 0

    date = 0
    while q:
        for _ in range(len(q)):
            cx, cy = q.popleft()

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0:
                    box[ny][nx] = 1
                    ripe_count += 1
                    q.append((nx, ny))
        date += 1

    return date - 1 if ripe_count == total_tomatoes - empty_area else -1

def main():
    m, n, box = get_input()
    print(bfs(m, n, box))

main()