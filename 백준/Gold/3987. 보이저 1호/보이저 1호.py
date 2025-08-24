from collections import deque


def move(ci, cj, cd):
    # [0] 필요한 자료형
    v = set()

    # [1] 첫방문
    v.add((ci, cj, cd))

    # [2] 전파
    cnt = 0
    while True:
        di, dj = delta[cd]
        ni, nj = ci + di, cj + dj
        cnt += 1

        if (not (1 <= ni <= N and 1 <= nj <= M)) or arr[ni][nj] == 'C':
            return cnt

        if (ni, nj, cd) in v:
            return -1

        if arr[ni][nj] == "\\":
            cd = 3 - cd
        elif arr[ni][nj] == "/":
            cd = (1 - cd) % 4

        v.add((ni, nj, cd))
        ci, cj = ni, nj  # 다음 작업 준비 계속 까먹는다 ex) 행렬 바꾸기, 현재 좌표 갱신하기

# 1. 시뮬레이션 준비
N, M = map(int, input().split())
arr = [['.']*(M+1)] + [['.']+list(input()) for _ in range(N)]
si, sj = map(int, input().split())

# 2. 시뮬레이션 실행
delta = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
ans = [-1, -1]
for sd in range(4):  # 위부터 체크
    cnt = move(si, sj, sd)
    if cnt == -1:
        ans = [['U', 'R', 'D', 'L'][sd], -1]
        break
    else:
        if cnt > ans[1]:
            ans[0] = ['U', 'R', 'D', 'L'][sd]
            ans[1] = cnt

# 3. 시뮬레이션 정답
print(ans[0])
print('Voyager' if ans[1] == -1 else ans[1])
