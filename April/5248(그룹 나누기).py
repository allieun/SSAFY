def find_parent(student, parent):
    # 내가 그룹의 대표라면 그대로 반환
    if parent[student] == student:
        return student
    
    # 대표를 찾을 때까지 부모를 따라 올라감
    parent[student] = find_parent(parent[student], parent)
    return parent[student]


def union_group(student1, student2, parent):
    # 각 학생의 대표 찾기
    root1 = find_parent(student1, parent)
    root2 = find_parent(student2, parent)

    # 이미 같은 그룹이면 아무것도 안 함
    if root1 == root2:
        return

    # 번호가 더 작은 쪽을 대표로 통일
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    신청정보 = list(map(int, input().split()))

    # 처음에는 모든 학생이 자기 자신이 대표
    parent = [i for i in range(N + 1)]

    # 신청서를 2개씩 묶어서 처리
    for i in range(0, 2 * M, 2):
        student1 = 신청정보[i]
        student2 = 신청정보[i + 1]
        union_group(student1, student2, parent)

    # 모든 학생의 대표를 한 번씩 정리
    for student in range(1, N + 1):
        find_parent(student, parent)

    # 대표자만 모아서 그룹 수 계산
    representatives = set()
    for student in range(1, N + 1):
        representatives.add(parent[student])

    print(f"#{tc} {len(representatives)}")

