def check(ci, cj, color):
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
        chg = []
        ni, nj = ci+di, cj+dj
        while True:
            if not (1 <= ni < 7 and 1 <= nj < 7):
                break

            if arr[ni][nj] == '.':
                break # debug: return -> break -> 다른 방향은 체크해야함
            elif arr[ni][nj] == color: # 같은색 돌: 그 사이 바꾸기
                for ti, tj in chg:
                    arr[ti][tj] = color
                break
            else: # 다른색 돌: 변경 대상
                chg.append((ni, nj))

            ni += di  # while문에서 이거 계속 빼먹음
            nj += dj


N = int(input())
arr = [['.']*7 for _ in range(7)]
arr[3][3] = arr[4][4] = 'W'
arr[3][4] = arr[4][3] = 'B'

for n in range(N) :
    # 1. 돌 입력 --> 돌 놓기
    ci, cj = map(int, input().split())
    arr[ci][cj] = 'B' if n%2 == 0 else 'W'

    # 2. 상대돌 뒤집을 수 있는지 확인 (4방향 : 행,열,대각선 확인)
    check(ci, cj, arr[ci][cj])



# 3. 정답 처리
w_cnt = b_cnt = 0
for i in range(1, 7):
    print(*arr[i][1:], sep='')
    for j in range(1, 7):
        if arr[i][j] == 'W':
            w_cnt += 1
        elif arr[i][j] == 'B':
            b_cnt += 1

# print('White' if w_cnt > b_cnt else 'B') # debug 5만시간 걸림.... 복붙은 정말 주의하자
print('White' if w_cnt > b_cnt else 'Black')




