from collections import deque

def bfs(si, sj, ei, ej):
    # [0] 필요한 자료형
    q = deque()
    v = [[0]*M for _ in range(N)]

    # [1] 첫방문
    q.append((si, sj))
    v[si][sj] = 1

    # [2] 순회
    while q:
        ci, cj = q.popleft()

        # 종료 조건
        if ci == ei and cj == ej :
            return v[ci][cj]-1
            """
            ※ -1 해줘야하는 이유 
            : 첫방문에서 실제 cnt는 0이지만 방문을 표시하기 위해 1 입력 
            -> 최종 결과에서 1이 증가해서 출력되므로, 마지막에 1을 빼줘야함 
            """

        # 인접 방문
        for di, dj in delta[ci%2] :
            ni, nj = ci+di, cj+dj

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            if not v[ni][nj] and adj[ni][nj] == 0 :
                v[ni][nj] = v[ci][cj]+1
                q.append((ni, nj))

    return -1

# 1. 그래프 만들기
N, M, K = map(int, input().split())
adj = [[0]*M for _ in range(N)]

# 장애물 배치
for _ in range(K) :
    i, j = map(int, input().split())
    adj[i][j] = -1

# 2. BFS
delta = [[(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)],
         [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]]
ANS = bfs(0, 0, N-1, M-1)

# 3. 정답 출력
print(ANS)
