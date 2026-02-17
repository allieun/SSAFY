'''
N x N 배열의 판에서 검정색을 피해 하얀색 공간에서 길이 k의 단어가 들어갈 경우의 수가 얼마인가? 를 구하는 문제
흰색 칸은 1, 검정색 칸은 0으로 인식한다.

1) 행 우선 순회 진행
2) 열 우선 순회 진행
3) 1이 나올 때 마다 카운트 해 나가며 카운트 한 값이 k와 같다면 정답의 경우의 수에 추가 (무작정 추가x)
4) 만약 0을 만나거나, 배열 끝 까지 갔을 때 카운트 한 숫자가 k와 같다면 정답의 경우의 수에 1을 추가
5) 최종적으로 테스트 케이스 번호와 정답값을 함께 출력
'''

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    answer = 0

    for r in range(n):                            # 행 우선 순회 진행
        count_r = 0
        for c in range(n):
            if grid[r][c] == 1:                   # 하얀색 칸일 때 1 추가
                count_r += 1
            if grid[r][c] == 0 or c == n-1:       # 배열의 끝까지 가거나 (마지막 열까지), 벽을 만날 때
                if count_r == k:                  # 카운팅 된 값이 k와 같은 지 확인
                    answer += 1                   # 같을 때는 정답 경우의 수 변수에 1 추가
                count_r = 0                       # 1 추가 후 다시 카운트 변수 0으로 초기화

    for c in range(n):                           # 열 우선 순회 진행
        count_c = 0
        for r in range(n):
            if grid[r][c] == 1:                  # 하얀색 칸일 때 1추가
                count_c += 1
            if grid[r][c] == 0 or r == n-1:      # 배열의 끝까지 가거나 벽을 만날 때
                if count_c == k:                 # 카운팅 된 값이 k와 같다면
                    answer += 1                  # 정답에 1 추가
                count_c = 0                      # 1 추가 후 다시 카운트 변수 0으로 초기화
    
    print(f'#{tc} {answer}')