def move(ci, cj, d):
    ni, nj = ci+dirs[d][0], cj+dirs[d][1]
    # 체스판 밖으로 나감
    if not (1 <= ni < 9 and 1 <= nj < 9) :
        return ci, cj # debug : cannot unpack non-iterable NoneType object

    # 돌이 있음
    if arr[ni][nj] == 'S':
        move(ni, nj, d)

    # 돌 이동 불가 -> 왕 이동 불가
    if arr[ni][nj] == 'S':
        return ci, cj

    # 이동
    arr[ni][nj] = arr[ci][cj]
    arr[ci][cj] = 0

    return ni, nj


# 0) 델타 좌표 만들기
dirs = {'R':(0, 1), 'L':(0, -1), 'B':(-1, 0), 'T':(1, 0), 'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}

# 1) 좌표 반영하기
arr = [[0]*9 for _ in range(9)]
K, S, N = input().split()

K = (int(K[1]), ord(K[0])-ord('A')+1)
arr[K[0]][K[1]] = 'K'
S = (int(S[1]), ord(S[0])-ord('A')+1)
arr[S[0]][S[1]] = 'S'

# 2) 이동하기
mi, mj = K[0], K[1]
for _ in range(int(N)):
    order = input()
    mi, mj = move(mi, mj, order)

# 3) 왕, 돌의 마지막 위치 (수가 작으므로 그냥 완전 탐색)
for i in range(1, 9):
    for j in range(1, 9):
        if arr[i][j] == 'K':
            print(chr(j+64)+str(i))

for i in range(1, 9):
    for j in range(1, 9):
        if arr[i][j] == 'S':
            print(chr(j+64)+str(i))