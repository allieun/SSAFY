'''
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 코드
처음에는 테스트케이스 수가 주어짐
그 다음에는 v 와 e가 주어짐(v : 노드 개수, e : 간선 정보 개수)
e개의 간선 정보가 주어지고, 마지막에 출발 노드 s 와 도착 노드 g가 주어짐

BFS로 푸는걸 추천함 (제미나이 추천)
'''

from collections import deque

def bfs(s, g, graph):    # bfs에 시작점과 도달점, 그리고 그래프에 대한 정보를 넣고 시작
    q = deque([s])       # 큐에 시작점을 넣고 시작
    visited[s] = 1       # 시작점은 방문처리
    while q:
        current = q.popleft()   # FIFO 규칙에 따라 현재 지점을 꺼냄
        if current == g:        # 현재 위치가 목표지점일 때는 1을 뺀다(시작점의 거리를 1로 잡아서)
            return visited[current]-1    
        for next_node in graph[current]:   # 현재 위치에서 이동 가능한 다음 노드에 대해서는
            if not visited[next_node]:     # 아직 방문하지 않았다면
                visited[next_node] = visited[current] +1    # 
                q.append(next_node)      # 큐에 넣어 다음에 방문해서 탐색할 수 있게 조치
    return 0                      # 없다면 0


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