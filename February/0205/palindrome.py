def is_palindrome(string):
    return string == string[::-1]                            # 테스트케이스 지정 이전에 회문을 판별하는 함수 지정

T = 10                                                       # 테스트 케이스 갯수 지정

for tc in range(1, T+1):
    N = int(input())
    grid = [list(input()) for _ in range(8)]                 # 8 x 8 배열의 2차원 배열 지정
    count = 0                                                # 회문 카운트할 개수 지정

    for r in range(8):                                       # 가로 방향 행 우선 순회에서의 회문 먼저 판별
        for c in range(8-N+1):
            row_string = ''.join(grid[r][c:c+N])             # c번 인덱스부터 c + N - 1번 인덱스까지 슬라이싱
            if is_palindrome(row_string):                    # 슬라이싱한 리스트가 회문일 경우 카운트 1 추가
                count += 1

    for c in range(8):                                      # 세로 방향 카운트 지정
        for r in range(8-N+1):
            column_string = ''                              # 세로 방향은 열 우선 순환으로 가야 하나?
            for dr in range(N):                             # 행이 먼저 움직이고 열은 그 다음
                column_string += grid[dr+r][c]

            if is_palindrome(column_string):
                count += 1
    print(f'#{tc} {count}')