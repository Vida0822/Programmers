"""
좌표 기준 : 목적지 기준 *** 으로 원본의 어느 좌표의 값이 저장되는지 확인
ex. 180도 회전 : narr[i][j] <- arr[N-1-i][M-1-j]
ex. 270도 회전 : narr[i][j] <- arr[j][N-1-i]
"""

def updwn():  # 1
    for j in range(M):
        for i in range(N//2):
            arr[i][j], arr[N-i-1][j] = arr[N-i-1][j], arr[i][j]

def lftrgt(): # 2
    for i in range(N):
        for j in range(M // 2):
            arr[i][j], arr[i][M-j-1] = arr[i][M-j-1], arr[i][j]


def rgh_rot() : # 3
    global N, M
    copy_arr = []

    for j in range(M):
        lst = [arr[i][j] for i in range(N-1, -1, -1)]
        copy_arr.append(lst)

    N, M = M, N
    return copy_arr

def lft_rot(): # 4
    global N, M
    copy_arr = []

    for j in range(M-1, -1, -1):
        lst = [arr[i][j] for i in range(N)]
        copy_arr.append(lst)
    N, M = M, N
    return copy_arr


def rgt_sft() : # 5
    for i in range(N//2):  # 각 부분집합의 1행
        lst = arr[i][:M//2] # 1행
        arr[i][:M//2] = arr[i+N//2][:M//2] # 1 <- 4
        arr[i + N//2][:M//2] = arr[i+N//2][M//2:]  # 4 <- 3
        arr[i+N//2][M//2:] = arr[i][M//2:] # 3 <- 2
        arr[i][M//2:] = lst   # 1 <- 2

def lft_sft() : # 6
    for i in range(N // 2):  # 각 부분집합의 1행
        lst = arr[i + N // 2][:M // 2] # 4행
        arr[i + N // 2][:M // 2] = arr[i][:M//2]  # 4 <- 1
        arr[i][:M//2] = arr[i][M//2:]  # 1 <- 2
        arr[i][M//2:] = arr[i+N//2][M//2:]  #  2 <- 3
        arr[i+N//2][M // 2:] = lst  # 3 <- 4



N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

orders = list(map(int, input().split()))
for ord in orders:
    if ord == 1:
        updwn()
    elif ord == 2:
        lftrgt()
    elif ord == 3:
        arr = rgh_rot()
    elif ord == 4 :
        arr = lft_rot()
    elif ord == 5:
        rgt_sft()
    else:
        lft_sft()

for a in arr:
    print(*a)

