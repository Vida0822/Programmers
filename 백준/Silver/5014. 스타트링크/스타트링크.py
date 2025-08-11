"""
아이디어 떠올리지 못해 결국 힌트('알고리즘 분류') 참고
--> 대놓고 BFS처럼 보이는게 아닌 문제에서 BFS를 떠올리기가 너무 어렵다 ㅠㅠ
--> 특징 정리 필요할 듯 ?
1. 시작점과 도착점이 있다
2. 최소 몇번만에, 최소 몇초만에.... 
3. 모든 층 연결 X , 특정 층끼리 연결

"""

from collections import deque

F, S, G, U, D = map(int, input().split())

def BFS():
    # [0] 필요한 자료형 정의
    q = deque()
    v = set()

    # [1] 첫방문
    q.append((S, 0))
    v.add(S)

    # [2] 인접 노드 방문
    while q:
        c, cnt = q.popleft()

        # 종료 조건
        if c == G:
            return cnt

        # 인접노드 방문
        for n in (c+U, c-D):
            # 범위, 미방문, 조건 검사
            if not 1 <= n <= F:
                continue

            if n not in v:
                v.add(n)
                q.append((n, cnt+1))
    else:
        return -1



ANS = BFS()
print(ANS if ANS != -1 else 'use the stairs')


