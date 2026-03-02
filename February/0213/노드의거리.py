'''
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 코드
처음에는 테스트케이스 수가 주어짐
그 다음에는 v 와 e가 주어짐(v : 노드 개수, e : 간선 정보 개수)
e개의 간선 정보가 주어지고, 마지막에 출발 노드 s 와 도착 노드 g가 주어짐

BFS로 푸는걸 추천함 (제미나이 추천)
'''

from collections import deque

def bfs(s, g, graph):
    q = deque([s])
    visited[s] = 1
    while q:
        current = q.popleft()
        if current == g:
            return visited[current]-1
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = visited[current] +1
                q.append(next_node)
    return 0


t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    s, g = map(int, input().split())
    answer = bfs(s, g, graph)

    print(f'#{tc} {answer}')