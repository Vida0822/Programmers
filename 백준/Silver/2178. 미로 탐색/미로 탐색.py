def bfs(i, j) :
    # 초기화
    v = [[0]*M for _ in range(N)]
    v[i][j] = 1
    q = [(i, j)]

    while q :
        ci, cj = q.pop(0)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj

            # 종료 조건
            if ni == N-1 and nj == M-1 :
                return v[ci][cj] + 1

            # 범위 체크 (index out of range)
            if not (0 <= ni < N and 0 <= nj < M) :
                continue

            if adj[ni][nj] != 0 :
                if v[ni][nj] == 0 :
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni, nj))

    # else :  --> 갈 수 없는 경우는 주어지지 않는다



N, M  = map(int, input().split())
adj = [list(map(int, input())) for _ in range(N)] # 행렬 그래프

print(bfs(0,0)) # 시작 위치를 (1, 1) --> (0,0)로 변경 (for 배열 index)