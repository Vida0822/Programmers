dirs = {1:(0, 1), 2:(0, -1), 3:(-1, 0), 4:(1,0)}

def move(ci, cj, comm) :
    # 1) 좌표 이동
    ni, nj = ci+dirs[comm][0], cj+dirs[comm][1]
    if not (0 <= ni < N and 0 <= nj < M):
        return ci, cj

    # 2) 주사위 상태값 바꾸기 (경우의 수가 많지 않기때문에 하드코딩)
    if comm == 1:
        t = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[3]
        dice[3] = t

    elif comm == 2:
        t = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = t

    elif comm == 3 :
        t = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[3]
        dice[3] = t

    elif comm == 4:
        t = dice[3]
        dice[3] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[0]
        dice[0] = t


    # 3) 바닥과의 상호작용
    if arr[ni][nj] == 0:
        arr[ni][nj] = dice[3]
    else:
        dice[3] = arr[ni][nj]
        arr[ni][nj] = 0

    # 4) 출력 : 주사위 윗면
    print(dice[1])

    return ni, nj

# 1. 입력받기 & 지도 만들기
N, M, ci, cj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 2. 각각의 command에 따라
dice = [0]*6
for comm in command:
    # 3. 이동
    ci, cj = move(ci, cj, comm)


