'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!

1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하이다.

'''

T = int(input())                                                                 # 테스트 케이스 T 입력

for tc in range(1, T+1):
    N, M = map(int, input().split())                                             # N(전체 배열), M(파리채 배열) 입력
    numrray = [list(map(int, input().split())) for _ in range(N)]                # N x N 기준으로 하는 전체 배열(2차원 생성)

    max_catch = 0                                                                # 파리채 배열 최대 합 임시값으로 지정

    for c in range(N-M+1):                                                       # c(열), r(행) 순서대로 행 우선 순회 지정
        for r in range(N-M+1):
            catch = 0                                                            # 파리채 배열 합 임시값 지정
            for dc in range(M):                                                  # 파리채 배열에서 행 우선 순회 설정 후 catch에 범위 값들을 하나씩 더해서 추가
                for dr in range(M):
                    catch += numrray[c+dc][r+dr]

            if catch > max_catch:
                max_catch = catch

    print(f'#{tc} {max_catch}')