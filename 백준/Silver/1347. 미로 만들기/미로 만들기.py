"""
조건
- R <= 50 , C <= 50

접근 방법
- F
    - ci, cj
    - delta[cd] -> di, dj -> ni, nj
    - 이동 : ci, cj = ni, nj
        --> 지도 확장
- R, L
    - cd = (cd+1)%4
"""


# [0] 준비
K = int(input())
orders = input()
delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

v = [[0]*100 for _ in range(100)]
ci, cj, cd = 50, 50, 3
v[ci][cj] = 1

# [1] 실행
# 1. 이동하기
up = lft = dwn = rgt = 50
for o in orders:
    # L or R : 회전
    if o == 'L' :
        cd = (cd-1)%4
    elif o == 'R':
        cd = (cd+1)%4
    else :
        # F : 전진
        di, dj = delta[cd]
        ni, nj = ci+di, cj+dj
        v[ni][nj] = 1

        up = min(up, ni)
        dwn = max(dwn, ni)
        lft = min(lft, nj)
        rgt = max(rgt, nj)

        ci, cj = ni, nj
debug = 0

# 2. 지도 만들기
v = [v[lft:rgt+1] for v in v[up:dwn+1]]
for i in range(len(v)):
    for j in range(len(v[0])):
        if not v[i][j] :
            v[i][j] = '#'
        else:
            v[i][j] = '.'
debug = 1

# [2] 출력
for vv in v :
    print(*vv, sep='')
debug = 2
