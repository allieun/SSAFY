'''
16 x 16 배열의 미로에서 (0, 0)을 기준으로 하여 가로 방향 x(c), 세로 방향 y(r)일 때,
미로 탐색의 시작은 (1, 1)에서 시작됨
2의 값을 가진 좌표에서 시작해서 3의 값을 가진 좌표까지의 도달 여부를 표시한다.
배열 안에서 1은 벽, 0은 이동 가능한 길, 2는 출발점, 3은 도착점

이 문제는 bfs를 활용해서 푸는 것이 일반적 -> 최단 경로 / 갈림길dptj


visited를 활용해서 푸는 문제
'''
from collections import deque

def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        if grid[r][c] == 3:
            return 1
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < 16 and 0 <= nc < 16:
                if grid[nr][nc] != 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
    return 0


t = 10

for tc in range(1, t+1):
    tc = int(input())
    grid = [list(map(int, input().strip())) for _ in range(16)]

    visited = [[0]*16 for _ in range(16)]
    for r in range(16):
        for c in range(16):
            visited[r][c] = 0

    answer = bfs(1, 1)
    print(f'#{tc} {answer}')
