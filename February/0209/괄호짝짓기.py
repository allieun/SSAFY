'''
4 종류의 괄호문자 '()', '[]', '{}', '<>' 로 이루어진 문자열
공백 문자 후 유효성 여부를 1 또는 0으로 표시 (1 - 유효함, 0 - 유효하지 않음)
'''


t = 10

for tc in range(1, t+1):
    n = int(input())
    character = input()

    stack = [0] * n
    top = -1
    answer = 1
    pairs = {')' : '(', ']': '[', '}' : '{', '>' : '<'}

    for char in character:
        if char in '([{<':
            top += 1
            stack[top] = char
        elif char in ')]}>':
            if top == -1 or stack[top] != pairs[char]:
                answer = 0
                break
            else:
                top -= 1

    if top != -1:
        answer = 0

    print(f'#{tc} {answer}')