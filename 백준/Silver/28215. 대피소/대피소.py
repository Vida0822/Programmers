def dfs(n, i, ans):
    global ANS_MIN

    # [0] 종료 조건
    if n == K:
        # 정답 처리
        dis = [200000]*N
        for si, sj in ans:
            for h in range(len(H)):
                ei, ej = H[h]
                dis[h] = min(dis[h], abs(si-ei)+abs(sj-ej))
                # print(si, sj, ei, ej, dis[h])

        t = max(dis)
        if t < ANS_MIN:
            ANS_MIN = t
        return


    # [1] 재귀 호출
    for j in range(i+1, N):
        ans.append(H[j])
        dfs(n+1, j, ans)
        ans.pop()

N, K = map(int, input().split())
H = [tuple(map(int, input().split())) for _ in range(N)]

ANS_MIN = 200000
dfs(0, 0, [])
print(ANS_MIN if ANS_MIN != 200000 else 0) # edge case : N == K
