

t = int(input())

for tc in range(1, t+1):
    code = input()
    stack = [0] * len(code)
    top = -1
    answer = 1

    for char in code:
        if char in '({':
            top += 1
            stack[top] = char
        elif char == ')':
            if top == -1 or stack[top] != '(':
                answer = 0
                break
            else:
                top -= 1
        elif char == '}':
            if top == -1 or stack[top] != '{':
                answer = 0
                break
            else:
                top -= 1
    if top != -1:
        answer = 0

    print(f'#{tc} {answer}') 