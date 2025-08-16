from heapq import heappush, heappop
INF = int(1e9)

# 1. 그래프 만들기
N = int(input())
M = int(input())
adj = [{} for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s][e] = min(adj[s].get(e, INF), w)  # debug: 계속 실수, list에 append 할 때는 튜플로

# 2. 다익스트라
S, E = map(int, input().split())

def dijkstra(S, E):

    # [0] 필요한 자료형
    D = {i:[INF, ''] for i in range(1, N+1)}  # 도착노드 : {비용, [경로]}
    # 'tuple' object does not support item assignment : tuple내 값을 변경하려고 해서 생기는 문제
    hq = []

    # [1] 첫 방문
    D[S] = (0, str(S)+' ')
    heappush(hq, (0, S))

    # [2] 순회
    while hq:
        cw, ci = heappop(hq)

        # 가지치기
        if D[ci][0] < cw:
            continue

        # 릴리즈
        for ni in adj[ci] :
            nw = adj[ci][ni]
            if D[ni][0] > D[ci][0]+nw :
                D[ni][0] = D[ci][0]+nw
                D[ni][1] = D[ci][1]+str(ni)+' '
                heappush(hq, (D[ni][0], ni))
              #  print(D)
    return D

D = dijkstra(S, E)


# 3. 정답 출력
print(D[E][0])
print(len(D[E][1].split()))
print(D[E][1])


