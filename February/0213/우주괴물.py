'''
일단 2차원 배열 안에서 2가 있는 곳을 찾음(1곳 밖에 없음)
그런 다음 그 곳에서 4방향으로(상하좌우) 움직이며 안전구역을 카운트 함
벽이 있는 곳(1인 곳)에 막히기 전까지는 직선으로 계속 공격 범위에 들어감.
따라서 1에 닿기 전까지의 부분은 안전구역으로 카운트 되면 안된다.

'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 2:
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]

                    while 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:                # 벽에 닿았을 경우 멈추고 해당 if문 탈출
                            break
                        if grid[nr][nc] == 0:                # 빈공간을 만났을 때
                            grid[nr][nc] = -1                # 1을 만나지 않았을 경우 -1로 바꿔서 공격 범위에 포함된다는 표시하기
                        
                        nr += dr[i]                          # 다음 칸으로 이동
                        nc += dc[i]                          # 다음 칸으로 이동

    count = 0
    for row in grid:
        count += row.count(0)

    print(f'#{tc} {count}')