"""
조건
- R x C : R <= 10, C <= 10

접근
모든 섬 포함하는 가장 작은 직사각형 ?

1. 바다 잠기기
2. 지도 크기 세기 (각 가장자리 index update)
3. 지도 출력하기
-> O(N^2)

"""
def oob(ni, nj) :
    return not (0 <= ni < R and 0 <= nj < C)

# [0] 준비
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# [1] 실행
# 1. 바다 잠기기 (완탐)
cp_arr = [lst[:] for lst in arr]

for ci in range(R):
    for cj in range(C):
        cnt = 0
        for di, dj in {(-1 ,0),(0, -1),(0, 1), (1, 0)}:
            ni, nj = ci+di, cj+dj

            # '또, 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.'
            if oob(ni, nj) or arr[ni][nj] == '.':
                cnt += 1


        if cnt >= 3 :
            cp_arr[ci][cj] = '.'

arr = cp_arr
debug = 1

# 2. 지도 크기 세기 (완탐)
up, lft = R, C
dwn, rgt = 0, 0

for i in range(R):
     for j in range(C):
         if arr[i][j] == 'X':
             up = min(up,  i)
             lft = min(lft, j)
             dwn = max(dwn, i)
             rgt = max(rgt, j)
debug = 2

# [2] 출력
for i in range(up, dwn+1):
    print(*arr[i][lft:rgt+1], sep='')
debug = 3


