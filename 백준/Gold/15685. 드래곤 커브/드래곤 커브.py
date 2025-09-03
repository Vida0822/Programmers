
from collections import deque
def make_curve(si, sj, sd, n):
    '''
    n 세대 드래곤 커브를 만드는 함수
    :param si, sj: 드래곤 커브 시작 위치
    :param sd: 시작 방향
    :param n: 목표 세대이자, n+1은 포함될 좌표 수
    :return: 드래콘 커브에 포함되는 좌표
    '''

    # [0] 필요한 자료형
    curve = []
    d_stack = []

    # [1] 첫방문
    # 0
    curve.append((si, sj))
    d_stack.append(sd)

    # 1
    di, dj = delta[sd]
    curve.append((si+di, sj+dj))
    d_stack.append(sd)

    # [2] 커브 만들기 (2세대 ~ n세대)
    for c in range(1, n+1):
        # new 부분
        l = len(curve)-1
        t = len(d_stack)-1
        n_stack = []
        for _ in range(l) :
            # 1. 현재 좌표
            ci, cj = curve[-1] # 이전 점 좌표
            cd = d_stack[t] # 남은 방향 중 끝 (역순)
            debug = 1

            # 2. new 커브 부분
            nd = (cd+1)%4 # 새로운 방향
            di, dj = delta[nd] # 델타 좌표
            ni, nj = ci+di, cj+dj

            curve.append((ni, nj))
            n_stack.append(nd)
            t -= 1
        d_stack.extend(n_stack)
        # d_stack = n_stack
        debug = 2
    debug = 7
    return curve


def count_rec(locations):
    '''

    :param locations: 모든 드레곤 코브에 포함되는 좌표 집합 (set)
    :return: 만들어지는 정사각형 개수
    '''
    ret = 0
    for i in range(100):
        for j in range(100): # 모든 칸에 대해
            ret += 1
            for ci, cj in ((i, j), (i+1, j), (i, j+1), (i+1, j+1)) :
                if (ci, cj) not in locations :
                    ret -= 1
                    break
        debug = 4
    return ret



# [0] 준비
N = int(input())

delta = {0: (0, 1), 1: (-1, 0), 2:(0, -1), 3:(1, 0)}  # →, ↑, ←, ↓
debug = 0

# [1] 실행
locations = set()
for i in range(N) :
    x, y, d, g = map(int, input().split())
    curve = make_curve(y, x, d, g)
    debug = 2
    for c in curve:
        locations.add(c)
    debug = 3

# [2] 정답
# 정사각형 세기
locations = set(sorted(locations))
ans = count_rec(locations)
debug = 4
print(ans)
