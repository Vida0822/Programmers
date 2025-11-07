def dfs(n, i, ans):
    global cnt
    # [0] 종료 조건
    if n == N:
        if sum(ans) == K : # 정답 조건
            cnt += 1

    # [1] 재귀 호출
    for j in range(i+1, 13):
        dfs(n+1, j, ans+[j])



T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0
    dfs(0, 0, [])

    print(f'#{t} {cnt}')