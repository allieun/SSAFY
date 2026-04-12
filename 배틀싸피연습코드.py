from collections import deque

# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
move_cmds = ["RA", "DA", "LA", "UA"]
fire_cmds = ["RF", "DF", "LF", "UF"]

actions = []

def bfs(H, W, map_data, start, target):
    q = deque([(start[0], start[1], [])])
    visited = [[False] * W for _ in range(H)]
    visited[start[0]][start[1]] = True

    while q:
        r, c, path = q.popleft()

        # 1. 현재 위치에서 적을 쏠 수 있는지 확인
        for i in range(4):
            for k in range(1, 4):
                nr = r + dr[i] * k
                nc = c + dc[i] * k

                # 맵 밖이거나 바위면 그 방향 탐색 중단
                if not (0 <= nr < H and 0 <= nc < W) or map_data[nr][nc] == 'R':
                    break

                # 적 발견
                if (nr, nc) == target:
                    return path + [fire_cmds[i]]

        # 2. 4방향 이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                if map_data[nr][nc] == 'G':
                    visited[nr][nc] = True
                    q.append((nr, nc, path + [move_cmds[i]]))

    return []



while True:
    # 입력 받기
    # map_data, my_pos, enemies ...

    H, W = len(map_data), len(map_data[0])
    target = enemies['X']

    if not actions:
        actions = bfs(H, W, map_data, my_pos, target)

    if actions:
        output = actions.pop(0)
    else:
        output = "S"

    # submit(output)
