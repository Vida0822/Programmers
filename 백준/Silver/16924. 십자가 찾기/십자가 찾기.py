def check(ci, cj) :
    cnt = 1
    while True:
        for di, dj in ((-cnt, 0), (cnt, 0), (0, -cnt), (0, cnt)) :
            ni, nj = ci+di, cj+dj

            if not (1 <= ni <= N and 1 <= nj <= M) :
                return cnt-1

            if arr[ni][nj] != '*':
                return cnt-1

        cnt += 1



N, M = map(int, input().split())
arr = [['.']*(M+1)]+[['.']+list(input()) for _ in range(N)]
v = [[0]*(M+1) for _ in range(N+1)]

ans = []
for i in range(2, N):
    for j in range(2, M):
        if arr[i][j] != '*':
            continue
        s = check(i, j)

        if s != 0 :
            ans.append((i, j, s))
            for sd in range(-s, s+1):
                v[i+sd][j] = 1
                v[i][j+sd] = 1

res = True
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == '*' and v[i][j] != 1 :
            res = False
            break


if res and len(ans) <= N*M:
    print(len(ans))
    for a in ans:
        print(*a)
else:
    print(-1)
