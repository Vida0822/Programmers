"""
1차 시도 : 메모리 초과...
2차 시도 : 성공 (154144KB, 184ms )

[구상]
특정 위치(x)에서 갈 수 있는 좌표는 x-1, x+1, x+X --> 각각을 요소로 그래프 연결
=> 그렇게 그래프 연결해가다가 K가 되면 return

[디버깅]
- x가 될 수 있는 0 <= nx <= 100000 외의 좌표까지 방문해서 메모리 초과 발생
=> 방문 배열, 큐에 넣을 수 제한
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
            if 0 <= nx <= 100000 : #  debug: 불필요하게 가능한 범위 외 수까지 방문 배열에 넣어서 생기는 문제
                v.add(nx)
                q.append((nx, t+1))
else:
    print(0)
