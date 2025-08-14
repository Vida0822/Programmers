from heapq import heappop, heappush

INF = int(1e9)

def dijkstra(si, sj):

    # [0] 필요한 자료형 정의
    hq = []

    # [1] 첫방문
    D[si][sj] = 0
    heappush(hq, (0, si, sj))
    ANS = adj[si][sj]

    # [2] 순회
    while hq:
        cd, ci, cj = heappop(hq)

        if D[ci][cj] < cd:
            continue

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            # 범위 체크, 방문 체크
            if not (0 <= ni < N and 0 <= nj < N) :
                continue

            # 최소값 갱신
            nd = adj[ni][nj]
            if D[ni][nj] > D[ci][cj]+nd:
                D[ni][nj] = D[ci][cj]+nd
                heappush(hq, (D[ni][nj], ni, nj))



TC = int(input())
for tc in range(1, TC+1) :
    N = int(input())
    adj = [list(map(int, input())) for _ in range(N)]

    D = [[INF]*100 for _ in range(100)]
    ANS = dijkstra(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')