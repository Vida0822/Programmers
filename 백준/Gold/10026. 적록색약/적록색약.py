from collections import deque

def bfs(si, sj, color):
    # [1] 초기 자료형
    q = deque()

    # [2] 시작 위치
    q.append((si, sj))
    v[si][sj] = 1

    # [3] 탐색 시작 (방문 표시만 하면됨)
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci+di
            nj = cj+dj

            if not (0 <= ni < N and 0 <= nj < N):
                continue

            if v[ni][nj] == 0 :
                if not color and adj[ci][cj] == adj[ni][nj]:
                    v[ni][nj] = 1
                    q.append((ni, nj))
                # elif color and (adj[ci][cj] in ('R', 'G') and adj[ni][nj] in ('R', 'G')) :
                elif color :
                    if (adj[ci][cj] in ('R', 'G') and adj[ni][nj] in ('R', 'G')) or adj[ci][cj] == adj[ni][nj]:
                        v[ni][nj] = 1
                        q.append((ni, nj))

N = int(input())
adj = [input() for _ in range(N)]

ans = []
# 1. 색약X 탐색
cnt = 0
v = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if v[i][j] == 0 :
            cnt += 1
            bfs(i, j, False)
ans.append(cnt)

# 2. 색약O 탐색
cnt = 0
v = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if v[i][j] == 0 :
            cnt += 1
            bfs(i, j, True)

ans.append(cnt)

print(*ans)