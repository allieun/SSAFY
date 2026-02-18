'''
체스 판에서 퀸을 몇 개 까지 놓을 수 있을까? 단, 퀸의 공격범위에 겹치지 않고
'''

def dfs(n):
    global answer
    if n == N:
        ans += 1
        return
 
    for j in range(N):
        if not v1[j] and not v2[n + j] and not v3[n - j + N]:
            v1[j] = v2[n + j] = v3[n - j + N] = True
            dfs(n + 1)
            v1[j] = v2[n + j] = v3[n - j + N] = False
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    v1 = [False] * (N + 1)      # 열
    v2 = [False] * (2 * N + 1)  # 우상향 대각선 (r+c)
    v3 = [False] * (2 * N + 1)  # 좌상향 대각선 (r-c+N)
     
    dfs(0)
    print(f"#{tc} {answer}")