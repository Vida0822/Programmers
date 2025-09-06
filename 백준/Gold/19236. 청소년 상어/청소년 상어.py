import copy

def print_arr(arr):
    for a in arr:
        print(a, sep='\t')
    print()

# [0]
arr = [[0]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = [data[2*j], data[2*j+1]-1] # 방향 idx : 1빼서 관리

# print_arr(arr)
delta = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


# [1]
def oob(ni, nj):
    return not (0 <= ni < 4 and 0 <= nj < 4)

def find_fish(idx, arr):
    '''
    특정 idx의 물고기 위치를 반환하는 함수
    (매번 swap 된 물고기 위치를 갱신하는게 어려워 완탐으로 수정)
    :param idx: 물고기 인덱스
    :return: 물고기 위치
    '''
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == idx:
                return i, j
    return -1, -1

def move_shark(si, sj, eat, arr):
    '''
    상어를 이동시키는 모든 경우의 수를 해보며 물고기 최대값 구하기
    :param fi, fj: 상어 위치
    :param eat: 현재까지 먹은 물고기 합
    :return:
    '''

    global ANS
    debug = 1

    # [1] 핵심 로직 : 물고기 이동
    for idx in range(1, 17):
        fi, fj = find_fish(idx, arr) # DEBUG!!! 수정된 배열에서 다시 찾아줘야함 (원본 X)
        if fi == -1 and fj == -1 :  # 이미 없는 물고기
            continue
        dr = arr[fi][fj][1]

        for _ in range(8):
            di, dj = delta[dr]
            ni, nj = fi+di, fj+dj

            # 범위 밖이거나 상어
            if oob(ni, nj) or arr[ni][nj][0] == 0 :
                dr = (dr+1)%8
                arr[fi][fj][1] = dr # DEBUG!!!!!!!! 물고기 방향도 계속 업데이트해야함!!!

            # 빈칸이거나 다른 물고기
            else:
                arr[fi][fj], arr[ni][nj] = arr[ni][nj], arr[fi][fj] # swap
                break
            debug = 0

    # [2] 재귀 호출
    sd = arr[si][sj][1]
    di, dj = delta[sd]
    for cnt in range(1, 4):
        ni, nj = si+di*cnt, sj+dj*cnt

        # 종료 조건 : 상어 더 이상 이동 불가
        if oob(ni, nj):
            # 정답 처리
            ANS = max(ANS, eat)
            debug = 3
            return

        # 빈칸이면
        if arr[ni][nj] == [-1, -1] :
            continue
        # arr = [lst[:] for lst in arr]

        narr = copy.deepcopy(arr)
        idx, dr = narr[ni][nj]
        narr[si][sj] = [-1, -1]
        narr[ni][nj] = [0, dr]  # 상어 이동
        move_shark(ni, nj, eat + idx, narr)


# Main
# 상어 입장
si, sj, sd = 0, 0, arr[0][0][1]
eat = arr[0][0][0]
arr[si][sj] = [0, sd]  # 상어 : 0 , 빈칸: -1

ANS = eat
move_shark(si, sj, eat, arr)

# [2]
print(ANS)

