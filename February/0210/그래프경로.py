'''
특정 두개의 경로에 노드가 존재하는지 여부 확인하기
경로가 있으면 1, 없으면 0 출력

'''

def path(current, goal, adj, visited):
    visited[current] = True
    
    if current == goal:
        return True
    
    for neighbor in adj[current]:
        if not visited[neighbor]:
            if path(neighbor, goal, adj, visited):
                return True
    return False


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        
    S, G = map(int, input().split()) # 출발 S, 도착 G
    visited = [False] * (V + 1)
    
    result = 1 if path(S, G, adj, visited) else 0
    print(f"#{tc} {result}")