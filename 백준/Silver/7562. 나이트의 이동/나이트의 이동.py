
def bfs(si, sj) :
    # 초기화
    v = [[0]*L for _ in range(L)] # 이걸 여기서 안하고 main 함수에서 해주면 테스트 케이스가 넘어갈때 초기화 안됨
    v[si][sj] = 1
    q = [(si, sj)]

    while q :
        ci, cj = q.pop(0)

        # 종료 조건
        if ci == G[0] and cj == G[1] :
            return v[ci][cj] -1

        for di, dj in ((-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1)) :
            ni,  nj = ci + di, cj + dj

            # 범위 체크
            if not (0 <= ni < L and 0 <= nj < L) :
                continue

            # 방문 X
            if v[ni][nj] == 0 :
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))

    return 0



T = int(input())

for _ in range(T) :
    # 1. 그래프 만들기
    L = int(input())
    adj = [[0]*L for _ in range(L)]

    S =tuple(map(int, input().split()))
    G =tuple(map(int, input().split()))

    # 탐색
    print(bfs(S[0], S[1]))