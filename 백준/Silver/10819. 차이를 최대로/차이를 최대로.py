"""
접근 : 순열
--> v 배열 필요
"""
def dfs(n, ans):
    global ANS

    # [0] 종료 조건
    if n == N:
        # 계산
        sm = 0
        for i in range(N-1) :
            sm += abs(ans[i]-ans[i+1])

        if ANS < sm :
            ANS = sm
        return

    # [1] 재귀 호출
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            ans.append(A[j])
            dfs(n+1, ans)
            v[j] = 0
            ans.pop()


N = int(input())
A = list(map(int, input().split()))

ANS = -100*N
v = [0]*N
dfs(0, [])

print(ANS)
