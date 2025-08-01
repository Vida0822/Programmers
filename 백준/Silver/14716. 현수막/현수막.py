from collections import deque
def bfs(si, sj):
    # [0] 필요한 자료형
    q = deque()

    # [1] 첫방문
    q.append((si, sj))

    # [2] 순회
    while q:
        ci, cj = q.popleft()

        for di, dj in (((-1, 0), (1, 0), (0, 1),(0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))):
            ni, nj = ci+di, cj+dj

            if not (0 <= ni < N and 0 <= nj < M) :
                continue
            if v[ni][nj] == 0 and adj[ni][nj] == 1 :
                v[ni][nj] = 1
                q.append((ni, nj))


N, M = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

cnt = 0
for i in range(N) :
    for j in range(M) :
        if adj[i][j] == 1 and v[i][j] == 0:
            cnt += 1
            bfs(i, j)
            # for vv in v :
            #     print(*vv)
            # print()

print(cnt)