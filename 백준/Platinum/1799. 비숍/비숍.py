N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

v1 = [0]*(2*N)
v2 = [0]*(2*N)

ANS = 0

def dfs(n, cnt):
    global ANS

    # [0] 종료조건
    if n == 2*N:
        if ANS < cnt:
            ANS = cnt
        return

    # [1] 재귀호출 **
    f = False
    for j in range(n+1): # 우상향 대각선 0~9번을 조사하면서
        if 0 <= n-j < N and 0 <= j < N and adj[n-j][j] == 1:
            if not v1[n] and not v2[N-1  +n  -2*j]:
                f = True
                v1[n] = v2[N-1  +n  -2*j] = 1
                dfs(n+1, cnt+1)
                v1[n] = v2[N-1  +n  -2*j] = 0
    if not f:
        dfs(n+1, cnt)


dfs(0, 0)
print(ANS)
