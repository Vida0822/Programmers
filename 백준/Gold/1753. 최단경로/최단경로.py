from heapq import heappush, heappop
# 1. 그래프 만들기
V, E = map(int, input().split())
K = int(input())
adj = [{} for _ in range(V+1)]
# heapq에 저장하면 자동으로 짧은 비용 간선먼저 조회하지만, E=300000이기 때문에 모두 저장+조회하는건 비효율적
# => 최소 거리 간선만 저장

for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = min(adj[s].get(e, 11), w) # 방향 그래프

# 2. 최단거리 구하기 (다익스트라)
INF = 10*200000+1
def dijkstra(S):
    # [0] 필요한 자료형
    hq = []
    d = [INF]*(V+1)

    # [1] 첫방문
    heappush(hq, (0, S))
    d[S] = 0

    # [2] 순회
    while hq:
        cw, ci = heappop(hq)

        # 가지치기
        if d[ci] < cw:
            continue

        for ni in adj[ci]:
            nw = adj[ci][ni]
            if d[ni] > d[ci]+nw:
                d[ni] = d[ci]+nw
                heappush(hq, (d[ni], ni))

    return d
d = dijkstra(K)

# 3. 정답 출력
for ans in d[1:]:
    print(ans if ans != INF else 'INF')

