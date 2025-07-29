def dfs(r, c) :
    v[r][c] = 1

    for dr, dc in (-1, 0) , (1, 0), (0, -1), (0, 1):
        nr = r + dr
        nc = c + dc

        if 0 <= nr < N and 0 <= nc < M :
            if graph[nr][nc] == 1 and v[nr][nc] == 0 :
                dfs(nr, nc)


import sys
sys.setrecursionlimit(10000)

T = int(input())
for _ in range(T) :

    # 그래프 만들기
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)] # 행렬 그래프

    for _ in range(K) :
        c, r = map(int, input().split())
        graph[r][c] = 1

    v = [[0]*M for _ in range(N)]

    # 완전 탐색
    res = 0
    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 1 and v[i][j] == 0:
                res += 1
#                print(i, j)
                dfs(i, j)

    print(res)


