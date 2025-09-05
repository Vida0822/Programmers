"""
1차 시도 : 시간 초과

2차 시도 : 시간 초과
- 수정: 모래가 있을때만 흩뿌려줌
- 수정: tlst, nlst 두번 생성하는거 리펙토링

3차 시도 :
배열을 직접 돌리지 말고, look up 테이블을 각 방향별로 다르게 참조
(그래도 좋은..연습했다..)

"""
import sys
input = sys.stdin.readline

# [0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ci, cj, dr = N//2, N//2, 0

percentage = [2, 10, 7, 1, 5, 10, 7, 1, 2]
look_left = [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (1, -1), (1, 0), (1, 1), (2, 0), (0, -1)]
look_down = [(0, -2), (1, -1), (0, -1), (-1, -1), (2, 0), (1, 1), (0, 1), (-1, 1), (0, 2), (1, 0)]
look_right = [(-2, 0), (-1, 1), (-1, 0), (-1, -1), (0, 2), (1, 1), (1, 0), (1, -1), (2, 0), (0, 1)]
look_up = [(0, -2), (-1, -1), (0, -1), (1, -1), (-2, 0), (-1, 1), (0, 1), (1, 1), (0, 2), (-1, 0)]
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

ANS = 0

# [1]
# def print_arr(arr):
#     for r in range(N):
#         for c in range(N) :
#             print(arr[r][c], end='\t')
#         print()
#     print()

def oob(ni, nj) :
    return not (0 <= ni < N and 0 <= nj < N)

def spread(yi, yj, look):
    global ANS

    sand = arr[yi][yj]
    arr[yi][yj] = 0
    used = 0

    for l in range(9):
        di, dj = look[l]
        per = percentage[l]

        ni, nj = yi + di, yj + dj
        per_sand = int(sand * per / 100)
        used += per_sand
        if oob(ni, nj):
            ANS += per_sand
        else:
            arr[ni][nj] += per_sand

    di, dj = look[-1]
    if oob(yi+di, yj+dj):
        ANS += (sand-used)
    else:
        arr[yi+di][yj+dj] += (sand-used)
    return arr


def move(yi, yj, dr):
    global arr
    if dr == 0:
        arr = spread(yi, yj, look_left)
        debug = 0
    elif dr == 1:
        # t_arr = list(map(list, zip(*arr)))
        # n_arr = [lst[::-1] for lst in list(map(list, zip(*arr)))]
        # n_arr = spread(yj, N-1-yi, n_arr) # DEBUG !!!!!!!!! 전치 행렬 할때는 항상 기준 i, j 좌표도 그에 맞게 바꿔줘야함 주의
        # arr = list(map(list, zip(*n_arr)))[::-1]
        spread(yi, yj, look_down)
        debug = 1
    elif dr == 2 :
        # arr = [lst[::-1] for lst in arr]
        # arr = spread(yi, N-1-yj, arr)
        # arr = [lst[::-1] for lst in arr]
        spread(yi, yj, look_right)
        debug = 2
    elif dr == 3:
        # t_arr = list(map(list, zip(*arr)))[::-1]
        # n_arr = [lst[::] for lst in list(map(list, zip(*arr)))[::-1]]
        # n_arr = spread(N-1-yj, yi, n_arr)
        # arr = list(map(list, zip(*n_arr[::-1])))
        spread(yi, yj, look_up)
        debug = 4
    debug = 5


# 1. 토네이도 이동
cnt_mx = 1
t = 1
test = [[0]*N for _ in range(N)]
for cnt_mx in range(1, N) :
    if cnt_mx == N-1:
        rec = 3
    else:
        rec = 2

    for i in range(rec):
        di, dj = delta[dr]
        for cnt in range(1, cnt_mx+1):
            # 이동
            ni, nj = ci+cnt*di, cj+cnt*dj # 와... 이거 ni, nj cnt로 쓸때 '*'로 쓰는 실수 개마니함..
            test[ni][nj] = t
            t+= 1
            # print_arr(test)
            # 이동 & 모래 흩뿌리기
            if arr[ni][nj]: # Refactoring : 모래 있을때만 흩뿌려줌
                move(ni, nj, dr)

        dr = (dr+1)%4
        ci, cj = ni, nj

# [2]
print(ANS)
