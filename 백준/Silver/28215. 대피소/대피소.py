import math
INF = math.inf

def dfs(n, i, ans):
    global ANS_MIN

    # [0] 종료 조건
    if n == K: # 조합을 완성했을 때
        # 정답 처리
        H_dis = [INF]*N # 각 집에서 대피소로의 거리

        for h in range(len(H)):  # 각 집에서
            for k in range(len(ans)) : # 각 대피소로의 거리를 구하고
                si, sj = H[h][0], H[h][1]
                ei, ej = ans[k][0], ans[k][1]
                # print(si, sj, '->', ei, ej)
                H_dis[h] = min(H_dis[h], abs(si-ei) + abs(sj-ej))

        ANS_MIN = min(ANS_MIN, max(H_dis))
        return


    # [1] 재귀 호출
    for j in range(i+1, N):
        ans.append(H[j])
        dfs(n+1, j, ans)
        ans.pop()

N, K = map(int, input().split())
H = [tuple(map(int, input().split())) for _ in range(N)]

ANS_MIN = INF
dfs(0, -1, [])
print(ANS_MIN if ANS_MIN != 2000000 else 0) # edge case : N == K
