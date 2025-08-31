from collections import deque

def move(balls):
    '''

    :param balls: 이동시킬 파이어볼들
    :return: X --> 그냥 v 배열에 표시한다.
    '''
    while balls:
        ci, cj, cm, cs, cd = balls.popleft()
        di, dj = delta[cd]
        ni, nj = (ci+di*cs)%N, (cj+dj*cs)%N

        v[ni][nj].append((cm, cs, cd))


def change(ci, cj, balls_many):
    '''

    :param balls_many: 2개 이상 존재하는 파이어볼 변형)
    :return: X -> 새롭게 이동할 파이어볼로 갱신
    '''
    global balls

    # 1. 합치기
    L = S = 0
    D = set()
    n = len(balls_many)
    while balls_many:
        cm, cs, cd = balls_many.popleft()
        L += cm
        S += cs
        D.add(cd%2)

    # 2. 나누기 (사라질수도)
    nm = L//5
    ns = S//n
    D = [0, 2, 4, 6] if len(D) <= 1 else [1, 3, 5, 7]

    if nm <= 0:
        return

    # 3. 이동 준비
    for i in range(4):
        balls.append((ci, cj, nm, ns, D[i]))


# [0] 준비
N, M, K = map(int, input().split())
balls = deque()
for _ in range(M):
    balls.append(list(map(int, input().split())))

delta = {
    7:(-1, -1), 0:(-1, 0), 1:(-1, 1),
    6: (0, -1),          2:(0, 1),
    5:(1, -1),4: (1, 0), 3: (1, 1)
}
v = [[deque() for _ in range(N)] for _ in range(N)] # ** 3차원 배열 만들기 무조건 암기
debug = 0

# [1] 실행
for _ in range(K):

    # 1. 이동하기
    move(balls)
    debug = 1

    # 2. 변형하기
    for i in range(N):
        for j in range(N):
            if len(v[i][j]) >= 2:
                change(i, j, v[i][j])
                debug = 2
            elif v[i][j] :
                balls.append((i, j, *v[i][j].popleft())) # 다시 이동 준비
                debug = 3

# 3. 마지막으로 위치해야할 파이어볼 배치
move(balls)

# [2] 출력
ANS = 0
for i in range(N):
    for j in range(N):
        if v[i][j]:
            for ball in v[i][j]:
                ANS += ball[0]
print(ANS)