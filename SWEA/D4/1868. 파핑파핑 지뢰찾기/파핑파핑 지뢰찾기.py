def check(ci, cj):
    for di, dj in ((-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)):
        ni, nj = ci + di, cj + dj

        if not (0 <= ni < N and 0 <= nj < N):
            continue
        if adj[ni][nj] == '*':
            return False
    else:
        return True


def bfs(si, sj): # 여기서 문제 발생! 클릭 한번으로 재귀적으로 뻗어나가기에 BFS 로 포함해줘야함

    # [0] 필요한 자료형 + 첫방문
    q = [(si, sj)]
    v[si][sj] = 1

    # [1] 순회
    while q :
        ci, cj = q.pop(0)
        for di, dj in ((-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 1),
                       (1, -1), (1, 0), (1, 1)):
            ni, nj = ci + di, cj + dj

            if not (0 <= ni < N and 0 <= nj < N) :
                continue


            if not v[ni][nj] and adj[ni][nj] == '.' :
                v[ni][nj] = 1
                if check(ni, nj): # 그 인접칸도 주변에 지뢰가 없는 칸이면
                    q.append((ni, nj)) # 큐에 삽입


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    adj = [list(input()) for _ in range(N)]

    ANS = 0
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j] and adj[i][j] == '.':
                if check(i, j):
                    ANS += 1
                    bfs(i, j)

    for i in range(N):
        for j in range(N):
            if not v[i][j] and adj[i][j] == '.':
                ANS += 1
                v[i][j] = 1

    print(f'#{tc} {ANS}')
