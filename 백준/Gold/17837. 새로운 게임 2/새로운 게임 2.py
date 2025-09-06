# [0]
N, K = map(int, input().split())
colors = [list(map(int, input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]

mal_map = dict() # 각 말 idx의 위치와 방향을 저장해놓는 자료형
for idx in range(1, K+1) :
    si, sj, sd = map(int, input().split())
    mal_map[idx] = (si-1, sj-1, sd-1)  # 패딩 사용 안하기 위함
    arr[si-1][sj-1].append(idx)

delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
debug = 0

# [1]
def oob(ni, nj) :
    return not (0 <= ni < N and 0 <= nj < N)

def change_mal_map(mals, ni, nj):
    for idx in mals:
        ci, cj, cd = mal_map[idx]
        mal_map[idx] = (ni, nj, cd)

def solve():
    ANS = 0
    while True :  # 종료 조건 : 말 개수 4개
        ANS += 1
        for idx in range(1, K+1):
            # 1. 이동 말 추출
            ci, cj, cd = mal_map[idx]

            t = arr[ci][cj].index(idx)
            mals = arr[ci][cj][t:]
            arr[ci][cj] = arr[ci][cj][:t]
            debug = 1

            # 2. 이동 칸 color 확인
            ni, nj = ci+delta[cd][0], cj+delta[cd][1]
            if oob(ni, nj) or colors[ni][nj] == 2 :  # 파란색 or 범위 밖
                # 이동 방향 반대
                if cd in (0, 2):
                    cd += 1
                else:
                    cd -= 1

                # 재 이동 시도
                ni, nj = ci+delta[cd][0], cj+delta[cd][1]
                if oob(ni, nj) or colors[ni][nj] == 2: # 범위 밖 or 파란색
                    ni, nj = ci, cj
                    arr[ni][nj].extend(mals)
                elif colors[ni][nj] == 0:  # 흰색
                    arr[ni][nj].extend(mals)
                elif colors[ni][nj] == 1:  # 빨간색
                    arr[ni][nj].extend(mals[::-1])
                    # arr[ni][nj] = arr[ni][nj][::-1]
                mal_map[idx] = (ni, nj, cd)
                debug = 4

            elif colors[ni][nj] == 0 : # 흰색
                arr[ni][nj].extend(mals)
                debug = 2
            elif colors[ni][nj] == 1 : # 빨간색
                # arr[ni][nj].extend(mals)
                arr[ni][nj].extend(mals[::-1])
                # arr[ni][nj] = arr[ni][nj][::-1]
                debug = 3

            change_mal_map(mals, ni, nj)

            # [0] 종료 조건
            if len(arr[ni][nj]) >= 4:
                return ANS

            debug = 5
        if ANS > 1000 :
            return -1

# [2]
print(solve())
