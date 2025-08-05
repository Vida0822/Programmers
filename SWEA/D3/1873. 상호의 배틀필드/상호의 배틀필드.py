"""
소요 시간: 7:50~8:30 (40분)
시도 횟수 : 1회
실행 시간 : 189 ms
메모리 : 65,024 kb
접근 : 딕셔너리를 활용해 각 명령어별 방향 결정, 각 방향별 델타 결정
"""

orders = {'U':'^', 'D':'v', 'L':'<', 'R':'>'}
dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def move(ci, cj, ord):

    # 방향 바꾸기
    nd = orders[ord]
    arr[ci][cj] = nd

    # new 좌표
    di, dj = dirs[nd]
    ni, nj = ci+di, cj+dj

    # 범위 체크
    if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == '.':
        # 이동하기
        arr[ni][nj] = arr[ci][cj]
        arr[ci][cj] = '.'
        return ni, nj
    else:
        return ci, cj


def shoot(ci, cj):
    di, dj = dirs[arr[ci][cj]]

    ni, nj = ci+di, cj+dj
    while 0 <= ni < H and 0 <= nj < W:
        # 종료 조건
        if arr[ni][nj] == '*':
            arr[ni][nj] = '.'
            break
        elif arr[ni][nj] == '#':
            break
        else:
            ni += di
            nj += dj


T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]

    si = sj = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] in ('^', 'v', '<', '>'):
                ci, cj = i, j

    N = int(input())
    ords = input()

    for o in ords:
        if o in ('U', 'D', 'L', 'R'):
            ci, cj = move(ci, cj, o)
        else:
            shoot(ci, cj)

    print(f'#{t}', end = ' ')
    for a in arr:
        print(*a, sep='')

