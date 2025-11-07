from collections import deque

# [0]
def bfs(si, sj):
    global N, K, arr, ans
    # [0]
    q = deque()
    v = set()

    # [1]
    q.append((si, sj, False, [(si, sj, arr[si][sj])])) # 시작점은 공사 X
    v.add((si, sj, False, si, sj))

    # [2]
    while q:
        ci, cj, flag, route = q.popleft()
        if ans < len(route):
            if len(route) == 6 :
                debug = 1

            ans = max(ans, len(route))
            debug = 1

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci+di , cj+dj

            # 범위 밖
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if (ni, nj, arr[ni][nj]) in route :
                continue

            ch = route[-1][2]
            if ch > arr[ni][nj]:  # 다음게 나보다 낮으면
                if (ni, nj, flag) not in v:
                    q.append((ni, nj, flag, route + [(ni, nj, arr[ni][nj])]))
                    v.add((ni, nj, flag, ci, cj))
            else: # 다음게 나보다 높으면
                if not flag: # 공사 안했으면
                    if ch > arr[ni][nj]-K and (ni, nj, True) not in v: # 깎았을 때 이전게 나보다 높으면
                        q.append((ni, nj, True, route + [(ni, nj, ch-1)]))
                        v.add((ni, nj, True, ci, cj))


def solve():
    # 1. 가장 높은 봉우리 찾기
    mx = max(list(max(row) for row in arr))
    candi = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == mx:
                candi.append((i, j))
    debug = 0

    # 2. 각 봉우리마다 BFS
    for si, sj in candi:
        bfs(si, sj)
    debug = 1
    return ans

## MAIN ##
TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    ANS = solve()
    print(f"#{tc} {ANS}")