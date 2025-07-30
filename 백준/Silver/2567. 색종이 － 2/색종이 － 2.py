"""
풀이 시간 : 60분
- 구상 : 40분, 구현 : 10분, 디버그 : 10분
"""

# 1. 색종이 칠하기 : 넓이 때와 유사 BUT 패딩 필요 (사각형 전체에)
N = int(input())
arr = [[0]*102 for _ in range(102)]

for _ in range(N) :
    sj,  si = map(int, input().split())

    for i in range(si+1, si+11) : # si ~ si+9
        for j in range(sj+1, sj+11):
            if arr[i][j] == 0: # 안칠해져있으면
                arr[i][j] = 1 # 칠하기

# 2. 둘레 체크
l = 0
for i in range(1, 101) :
    for j in range(1, 101) :
        if arr[i][j] == 1 :
            cnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
                ni, nj = i+di, j+dj
               # if not (ni < 100 and 0 <= nj < 100) : --> 패딩 사용해서 필요 X
                #    break
                if arr[ni][nj] != 1:
                    cnt += 1
            if cnt > 0 :
                l += cnt

print(l)



