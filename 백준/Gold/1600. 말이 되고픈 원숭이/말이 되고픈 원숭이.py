from collections import deque

def bfs(si, sj):
    # [0] 필요한 자료형
    q = deque()
    v = set()
    ans = int(1e9)

    # [1] 첫방문
    q.append((si, sj, K, 0))
    v.add((si, sj, K))

    # [2] 순회
    while q:
        ci, cj, k, cnt = q.popleft()

        # 종료 조건
        if ci == N-1 and cj == M-1:
            ans = min(ans, cnt)

        # 인접 조회
        if k > 0:
            for di, dj in ((-1, -2), (-2, -1), (-1, 2), (-2, 1),
                           (1, -2), (2, -1), (1, 2), (2, 1)) :
                ni, nj = ci+di, cj+dj

                # 범위
                if not (0 <= ni < N and 0 <= nj < M):
                    continue

                if arr[ni][nj] == 1:
                    continue

                # 미방문, 조건
                if (ni, nj, k-1) not in v:
                    v.add((ni, nj, k-1))
                    q.append((ni, nj, k-1, cnt+1))

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            # 범위
            if not (0 <= ni < N and 0 <= nj < M):
                continue

            if arr[ni][nj] == 1:
                continue

            # 미방문, 조건
            if (ni, nj, k) not in v:
                v.add((ni, nj, k))
                q.append((ni, nj, k, cnt+1))

    # for vv in v :
    #     print(*vv)
    return ans if ans != int(1e9) else -1


### MAIN
K = int(input())
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


ANS = bfs(0, 0)
if arr[N-1][M-1] == 1 :
    print(-1)
else :
    print(ANS)