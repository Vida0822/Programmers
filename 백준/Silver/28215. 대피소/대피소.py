def dfs(n, i, ans):
    global ANS_MIN

    # [0] 종료 조건
    if n == K:
        # 정답 처리
        dis = [200000]*N
        for si, sj in ans: # 각 대피소에서
            for h in range(len(H)): # 모든 집으로의 거리를 구하고
                ei, ej = H[h]
                dis[h] = min(dis[h], abs(si-ei)+abs(sj-ej)) # 그 중 가장 작은 값을 해당 집과 대피소와의 거리로 설정
                # print(si, sj, ei, ej, dis[h])

        t = max(dis) # 그 거리 중 가장 큰 값 갱신 
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

ANS_MIN = 200001
dfs(0, 0, [])
print(ANS_MIN if ANS_MIN != 200001 else 0) # edge case : N == K
