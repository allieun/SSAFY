'''
더하기로만 이루어진 식을 계산해서 합계를 내보는 문제
후위연산식 활용하는 문제
'''


t = 10

for tc in range(1, t+1):
    num_len = int(input())
    case = input()

    stack = []
    postfix = ''

    for char in case:
        if '0' <= char <= 9:
            postfix += char
        else:
            while stack:
                postfix += stack.pop()
            stack.append(char)

    cal_stack = []
    for char in postfix:
        if '0' <= char < 9:
            cal_stack.append(int(char))
        else:
            n2 = cal_stack.pop()
            n1 = cal_stack.pop()
            cal_stack.append(n1+ n2)

    print(f'#{tc} {cal_stack.pop()}')
