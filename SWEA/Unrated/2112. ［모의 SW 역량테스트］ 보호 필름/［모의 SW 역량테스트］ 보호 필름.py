def check(arr):
    for j in range(M) : # 열 하나씩 검사
        cur = arr[0][j]
        cnt = 1
        mx = 0

        for i in range(1, N):
            if cur == arr[i][j] : # nxt
                cnt += 1
            else:
                mx = max(mx, cnt)
                cur = arr[i][j]
                cnt = 1
        mx = max(mx, cnt) # 연속된 값 체크할때 마지막거 체크하는거 계속 빼먹는다 ㄹㅈㄷ
        if mx < K :
            return False
    return True


def spread(typ, n, arr): # 뿌릴 약품, 행번호, 변화대상 격자
    narr = [lst[:] for lst in arr]

    for j in range(M) :
        narr[n][j] = typ

    return narr
    # if check(narr):
    #     return narr
    # else:
    #     return []


def dfs(n, cnt, arr):
    global ans

    # 가지치기
    if cnt > ans :
        return

    # [0] 종료 조건
    if n == N:
        if check(arr):
            ans = min(ans, cnt)
        return

    if cnt == 0:
        debug = 1
    if cnt == 1 :
        debug = 1
    # [1] 핵심 로직 : 약품 A/B/X
    narr = spread(0, n, arr) # 약품 뿌릴 행
    dfs(n+1, cnt+1, narr)

    narr = spread(1, n, arr) # 약품 뿌릴 행
    dfs(n+1, cnt+1, narr)

    narr = [lst[:] for lst in arr]
    dfs(n+1, cnt, narr)


TC = int(input())
for tc in range(1, TC+1):

    # [0]
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = N+10
    dfs(0, 0, arr)
    print(f"#{tc} {ans}")