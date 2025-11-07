from collections import deque

def oob(ni, nj, N) :
    return not (0 <= ni < N and 0 <= nj < N)

def solve():
    # [0]
    N, M, K = map(int, input().split())
    # arr = [[-1]*N]+[[-1]+[[] for _ in range(N-2)]+[-1] for _ in range(N-2)] + [[-1]*N]
    arr = [[[] for _ in range(N)] for _ in range(N)]

    for idx in range(1, K+1):
        si, sj, cnt, sd = map(int, input().split())
        arr[si][sj].append((sd-1, cnt))

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    debug = 0


    # [1]
    for _ in range(M):
        narr = [[[] for _ in range(N)] for _ in range(N)]
        for i in range(N) :
            for j in range(N):
                if arr[i][j] :
                    debug = 3
                    # 0. 검사할 군집 pop
                    ci, cj = i, j
                    cd, cnt = arr[ci][cj][0]

                    # 1. 이동
                    ni, nj = ci+delta[cd][0], cj+delta[cd][1]

                    # 2. 조건 검사
                    if oob(ni, nj, N) :
                        continue

                    if ni in (0, N-1) or nj in (0, N-1) :  # 약품인 경우
                        cnt //= 2
                        cd += (1 if cd in (0, 2) else -1)

                    # map 변경
                    # narr[ci][cj] = []
                    if cnt > 0 :
                        narr[ni][nj].append((cd, cnt))
        debug = 1

        # 3. 2개이상 군집 존재
        for i in range(N) :
            for j in range(N):
                if len(narr[i][j]) > 1 :
                    sm = sum(e[1] for e in narr[i][j])
                    mx = max(narr[i][j], key=lambda x: x[1])
                    narr[i][j] = [(mx[0], sm)]
        debug = 2
        arr = narr

    # 정답 도출
    ANS = 0
    for i in range(N):
        for j in range(N) :
            if arr[i][j]:
                ANS += arr[i][j][0][1]
    debug = 3
    return ANS

##################################################
TC = int(input())
for tc in range(1, TC+1):
    ANS = solve()
    print(f'#{tc} {ANS}')