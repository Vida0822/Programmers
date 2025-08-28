from collections import deque

can_go = {
    1:[(0, -1), (-1, 0), (0, 1), (1, 0)],
    2:[(-1, 0), (1, 0)],
    3:[(0, -1), (0, 1)],
    4:[(-1, 0), (0, 1)],
    5:[(1, 0), (0, 1)],
    6:[(0, -1), (1, 0)],
    7:[(0, -1), (-1, 0)]
}

def oob(ni, nj):
    return not (0 <= ni < N and 0 <= nj < M)

def bfs(si, sj, L):
    # [0] 필요한 자료형
    global ANS
    q = deque()
    v = [[0]*M for _ in range(N)]

    # [1] 첫방문
    q.append((si, sj))
    v[si][sj] = 1

    # [2] 순회
    while q:
    # for _ in range(L):
        ci, cj = q.popleft()
        t = A[ci][cj]

        for di, dj in can_go[t]:
            ni, nj = ci+di, cj+dj
            if oob(ni, nj):
                continue
            if v[ni][nj] or not A[ni][nj] :
                continue

            # 조건 :연결된 터널 ?
            tur = A[ni][nj]
            if (-di, -dj) in can_go[tur] :
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1
    debug = 0

    for i in range(N):
        for j in range(M):
            if v[i][j] <= L and v[i][j] != 0:
                ANS += 1




TC = int(input())
for tc in range(1, TC+1):

    # [0] 준비
    N, M, R, C, L = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # [1] 실행
    ANS = 0
    bfs(R, C, L) # si, sj, time 제한



    # [2] 정답 출력
    print(f'#{tc} {ANS}')