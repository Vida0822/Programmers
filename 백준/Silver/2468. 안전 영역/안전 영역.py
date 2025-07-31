"""

"""
def bfs(si, sj) :
    # [0] 필요한 자료형 선언
    q = []

    # [1] 시작 위치
    q.append((si, sj))
    v[si][sj] = 1

    # [2] 인접 노드 방문
    while q:
        ci, cj = q.pop()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci+di, cj+dj

            if not (0 <= ni < N and 0 <= nj < N) :
                continue
            if v[ni][nj] == 0 and adj[ni][nj] > H :
                q.append((ni, nj))
                v[ni][nj] = 1



N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
# v = [[0]*N for _ in range(N)]

ans = 0
for H in range(101) :
    v = [[0] * N for _ in range(N)] # 방문 배열은 높이때마다 초기화
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and adj[i][j] > H :
                cnt += 1
                bfs(i, j) # 방문 표시만

    ans = max(ans, cnt)

print(ans)
