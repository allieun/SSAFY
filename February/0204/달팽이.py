'''
기존에 달팽이 문제를 행 우선순회와 열 우선 순회를 사용해서 풀었기 떄문에, 이번에는 델타를 활용해서 풀어보려고 함

이동 순서는 우 -> 하-> 좌 -> 상이 반복되는 구조
델타 이동 방향을 우선적으로 지정한 뒤 

'''

t = int(input())

for tc in range(1, t+1):
    n= int(input())
    grid = [[0]*n for _ in range(n)]             # n x n 배열의 표 지정하기

    dr = [0, 1, 0, -1]                           # 우 하 좌 상
    dc = [1, 0, -1, 0]

    r, c = 0, 0                                  # 시작 좌표
    distance = 0                                 # 이동 방향

    for num in range(1, n*n+1):
        grid[r][c] = num                         # n x n 범위 에서 1부터 하나씩 채우기


        nr = r + dr[distance]
        nc = c + dc[distance]

        if nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] != 0:
            distance = (distance+1) % 4          # 4로 나놨을 때 나머지 1 2 3 0 인 이유는 dr과 dc가 4개의 눈금을 가지고 있기 때문
            nr = r + dr[distance]                # 오른쪽으로 가다 막히면 아래로, 아래로 가다 막히면 왼쪽으로 틀 수 있게 설정하는 것
            nc = c + dc[distance]

        r, c = nr, nc

    print(f'#{tc}')
    for row in grid:
        print(*row)