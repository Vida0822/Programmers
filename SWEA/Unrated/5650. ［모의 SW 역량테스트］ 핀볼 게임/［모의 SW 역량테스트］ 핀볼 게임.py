from collections import defaultdict

# [0] 전처리
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 나중에 옮기자
blocks = [  # 1-based
    [],
    [2, 2, -1, 1],
    [1, 2, 2, -1],
    [-1, 1, 2, 2],
    [2, -1, 1, 2],
    [2, 2, 2, 2]
]


# [1]
def oob(ni, nj):
    return not (0 <= ni < N and 0 <= nj < N)


def move(si, sj, dr): # *** MAIN
    # print(si, sj, dr)
    ci, cj = si, sj
    scr = 0

    while True :
        di, dj = delta[dr]
        ni, nj = ci+di, cj+dj  # new 좌표

        # 조건 검사
        # 1. oob
        if oob(ni, nj):
            scr += 1
            dr = (dr+2)%4  # ci, cj 는 변화

            ni, nj = ci, cj

        # 2. block
        if 1 <= arr[ni][nj] <= 5:
            scr += 1
            dr = (dr+blocks[arr[ni][nj]][dr])%4
            ci, cj = ni, nj # 일단 이동 : 갔다가 꺽는거라고 생각 (?)

        # 3. while holl
        elif 6 <= arr[ni][nj] <= 10:
            lst = white_holl[arr[ni][nj]]
            idx = lst.index((ni, nj))
            ci, cj = lst[(idx+1)%2]
            # 방향은 안바뀜

        # 4. black holl (종료조건 1)
        elif arr[ni][nj] == -1:
            return scr

        # 6. 빈칸
        else:
            # 5. 자신의 출발 위치 (종료조건 2)
            if (ni, nj) == (si, sj):
                return scr
            ci, cj = ni, nj  # 방향은 유지


def solve():
    mx = -1
    # 1. 모든 좌표, 모든 방향에 대해 완탐
    for si in range(N):
        for sj in range(N):
            if arr[si][sj] == 0 :

                # 2. 이동 시키기
                for sd in range(4):
                    if (si, sj) == (0, 9):
                        debug = 0
                    scr = move(si, sj, sd)
                    mx = max(mx, scr)

    return mx


TC = int(input())
for tc in range(1, TC+1):
    # [0]
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 화이트홀
    white_holl = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10 :
                white_holl[arr[i][j]].append((i, j))

    ans = solve()
    print(f"#{tc} {ans}")
