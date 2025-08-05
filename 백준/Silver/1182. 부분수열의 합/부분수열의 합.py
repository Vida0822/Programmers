def dfs(n, i, ans):
    global cnt

    # [0] 종료 조건
    if n == k:
        if sum(ans) == S: # 정답 조건
            cnt += 1

    # [1] 재귀 호출
    for j in range(i+1, N+1):
        if v[j] == 0:
            v[j] = 1
            ans.append(lst[j])
            dfs(n+1, j, ans)
            v[j] = 0
            ans.pop()


N, S = map(int, input().split())
lst = [0]+list(map(int, input().split()))
cnt = 0

for k in range(1, N+1):
    v = [0]*(N+1)
    dfs(0, 0, [])

print(cnt)