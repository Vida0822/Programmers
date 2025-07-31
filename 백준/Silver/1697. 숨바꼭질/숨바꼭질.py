"""
1차 시도 : 메모리 초과...

"""
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 그래프 만들기 & 찾기
# [1] 초기 자료형
v = set()
q = deque()

# [2] 초기값 삽입
q.append((N, 0))
v.add(N)

# [3] 인접 노드 방문
while q:
    x, t = q.popleft()

    if x == K :
        print(t)
        break

    for dx in (-1, 1, x) :
        nx = x + dx
        if nx not in v :
            if nx <= 100000 :
                v.add(nx)
                q.append((nx, t+1))
else:
    print(0)
