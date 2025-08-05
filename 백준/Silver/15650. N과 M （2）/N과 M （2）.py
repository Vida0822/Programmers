def dfs(m,i, ans):

    # [0] 종료 조건
    if m == M:
        print(*ans)
        return

    # [1] 재귀 호출
    for j in range(i+1, N+1):
            dfs(m+1,j, ans+[j])


N, M = map(int, input().split())
v = [0]*(N+1)
dfs(0,0, [])
