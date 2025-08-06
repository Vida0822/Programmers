def dfs(n, cw):
    global ANS
    # print(n, cw)

    # 가지치기
    if cw < 500:
        return

    # [0] 종료 조건
    if n == N:
        # cw -= K --> debug : dfs 호출할때 빼고 넣어주기 때문에 할필요X
        if cw >= 500:
            ANS += 1
        return

    # [1] 재귀 호출
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, cw+A[j]-K)
            v[j] = 0


N, K = map(int, input().split())
A = list(map(int, input().split()))

v = [0]*N
ANS = 0
dfs(0, 500)
print(ANS)