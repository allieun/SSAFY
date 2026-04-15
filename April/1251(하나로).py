import heapq
import sys

# 속도를 위해 입력 함수 교체
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    # 방문 여부 체크
    visited = [False] * N
    # 우선순위 큐: (비용, 정점번호)
    # 0번 섬에서 시작한다고 가정
    pq = [(0, 0)]
    
    total_dist_sq = 0
    count = 0
    
    while pq:
        dist_sq, now = heapq.heappop(pq)
        
        # 이미 방문한 섬이면 패스
        if visited[now]:
            continue
            
        # 방문 처리 및 비용 합산
        visited[now] = True
        total_dist_sq += dist_sq
        count += 1
        
        # 모든 섬을 연결했다면 종료
        if count == N:
            break
            
        # 현재 섬(now)에서 갈 수 있는 다른 섬들의 거리를 큐에 삽입
        for next_node in range(N):
            if not visited[next_node]:
                cost = (X[now] - X[next_node])**2 + (Y[now] - Y[next_node])**2
                heapq.heappush(pq, (cost, next_node))

    ans = total_dist_sq * E
    print(f"#{tc} {int(ans + 0.5)}")