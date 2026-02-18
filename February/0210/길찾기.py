'''
테스트 케이스 10개
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답(가능 여부)을 출력
가능할 경우에는 1 출력, 불가능하다면 0 출력
'''

def path(now):
    if now == 99:
        return True
    if now == -1 or visited[now]:
        return False
    visited[now] = True

    if path(adj_1[now]) or path(adj_2[now]):
        return True
    return False

t = 10

for _ in range(1,t+1):
    tc, n = map(int, input().split())
    route = list(map(int, input().split()))

    visited = [False]*100
    adj_1 = [-1] * 100
    adj_2 = [-1] * 100

    for i in range(n):
        start = route[2 *i]
        end = route[2 * i+1]

        if adj_1[start] == -1:
            adj_1[start] = end
        else:
            adj_2[start] = end

    answer = 1 if path(0) else 0
    print(f'#{tc} {answer}')