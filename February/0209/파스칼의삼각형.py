'''
양 끝에는 1이 입력되고, 가운데는 그 옆과 더한수가 들어감
1
1 2 1
과 같은 형태로 출력되어야 함
삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력해야 함
'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    pascal = [[1]]

    for i in range(1, n):
        prev = pascal[-1]
        new_pascal = [1]

        for j in range(len(prev)-1):
            new_pascal.append(prev[j]+prev[j+1])
        new_pascal.append(1)
        pascal.append(new_pascal)

    print(f'#{tc}')
    for row in pascal:
        print(*row)