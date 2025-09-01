"""
리펙토링 포인트 : 몸통을 일일히 이동시키지 않아도 된다
- 머리는 appendleft()로 무조건 새 좌표 추가
- 꼬리는 사과가 없을 때만 빼주기 (그게 기존 머리일수도 있음)
=> 자동으로 몸통이 늘어나거나 줄어드는 효과

"""
from collections import deque

def oob(ni, nj):
    return not (0 <= ni < N and 0 <= nj < N)

# [0] 준비
N = int(input())
K = int(input())

arr = [[0]*N for _ in range(N)] # NxN

# 사과 배치
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

# 뱀 회전 정보
L = int(input())
turn_map = dict()

for _ in range(L):
    X, C = input().split()
    turn_map[int(X)] = C

delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# [1] 실행
snake = deque([(0, 0)])
d = 2

time = 0 # ANS
while True :

    # 0. 시간 증가
    time += 1

    ci, cj = snake[0]
    di, dj = delta[d]
    ni, nj = ci+di, cj+dj

    # 1. 종료 조건
    if oob(ni, nj) or (ni, nj) in snake:
        break

    # 2. 머리 이동
    snake.appendleft((ni, nj))

    # 3. 사과 확인
    if arr[ni][nj] == 1:  # 사과면
        arr[ni][nj] = 0
    else:
        snake.pop()

    # 4. 방향 전환
    if time in turn_map:
        C = turn_map[time]
        ni, nj = snake[0]
        if C == 'L' :
            d = (d-1)%4
        else:
            d = (d+1)%4

# [2] 정답
print(time)