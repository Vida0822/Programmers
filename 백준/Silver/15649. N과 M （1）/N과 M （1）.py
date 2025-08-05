def dfs(m, ans):
    global v

    # [0] 종료 조건
    if m == M:
        print(*ans)
        return

    # [1] 재귀 호출
    for j in range(1, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(m+1, ans+[j])
            v[j] = 0 # debug 


N, M = map(int, input().split())
v = [0]*(N+1)
dfs(0, [])
