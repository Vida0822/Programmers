def dfs(n, sm, v):
    global ANS
    
    # 가지 치기 (debug) --> 가장 위에
    if sm > ANS :
        return

    # [0] 종료 조건
    if n == N:
        ANS = min(ANS, sm)
        return

    # [1] 재귀 호출
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm+arr[n][j], v)
            v[j] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ANS = 99*N
    dfs(0, 0, [0]*N)
    print(f'#{t} {ANS}')
