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

Refactoring : 방문 배열을 따로 만들지 않고, 바로 지도(arr)에 '.' 표시
=> 포함 부분만 출력
"""


# [0] 준비
K = int(input())
orders = input()
delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

arr = [['#']*100 for _ in range(100)]
ci, cj, cd = 50, 50, 3
arr[ci][cj] = '.'

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
        arr[ni][nj] = '.'

        up = min(up, ni)
        dwn = max(dwn, ni)
        lft = min(lft, nj)
        rgt = max(rgt, nj)

        ci, cj = ni, nj
debug = 0

# [2] 출력
for i in range(up, dwn+1):
    print(*arr[i][lft:rgt+1], sep='')
debug = 1

