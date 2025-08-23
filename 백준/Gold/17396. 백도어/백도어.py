from heapq import heappush, heappop

def dijkstra(s, e):
    # [0] 필요한 자료형
    D = [INF]*N
    hq = []

    # [1] 첫 방문
    D[s] = 0
    heappush(hq, (0, s))

    # [2] 순회
    while hq:
        cw, ci = heappop(hq)

        # 가지치기
        if D[ci] < cw:
            continue

        # 인접 방문
        for ni, nw in adj[ci]:
            if A[ni] == 1 and ni < e :
                continue
            if D[ni] > D[ci] + nw:
                D[ni] = D[ci] + nw
                heappush(hq, (D[ni], ni))

    return D[e] if D[e] != INF else -1


# 1. 그래프 입력
N, M = map(int, input().split())
A = list(map(int, input().split()))
INF = 300000*N + 1

adj = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    adj[a].append((b, t))
    adj[b].append((a, t))


# 2. 다익스트라
ANS = dijkstra(0, N-1)

# 3. 정답 출력
print(ANS)