from heapq import heappush, heappop

# 1. 문제 조건 만들기
N, M = map(int, input().split())
si, sj, ei, ej  = map(int, input().split())
adj = [['0']*(M+1)]+[['0']+list(input()) for _ in range(N)]

# 2. BFS
def bfs(si, sj, ei, ej):

    # [0] 필요한 자료형
    hq = []
    v = [[0]*(M+1) for _ in range(N+1)]

    # [1] 첫방문
    heappush(hq, (1, si, sj))
    v[si][sj] = 1

    # [2] 순회
    while hq:
        cnt, ci, cj = heappop(hq)

        # 종료 조건
        if ci == ei and cj == ej :
            return cnt

        # 인접 방문
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            # 범위, 미방문, 조건체크
            if 1 <= ni <= N and 1 <= nj <= M and not v[ni][nj] :
                v[ni][nj] = 1
                if adj[ni][nj] == '1' :
                    heappush(hq, (cnt+1, ni, nj))

                elif adj[ni][nj] == '0' :
                    heappush(hq, (cnt, ni, nj))

    return -1 # 나올 수 없음

adj[ei][ej] = '0'
print(bfs(si, sj, ei, ej))
