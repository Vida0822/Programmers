"""
전혀 모르겠어서 도움 받음 ㅠㅠ
"""

from collections import deque

t = int(input())
for _ in range(t) :

    # 1. 그래프 만들기 **
    N = int(input())

    ipt = []
    for i in range(N+2):
        x, y = map(int, input().split())
        ipt.append([i, x, y])

    adj = [[] for _ in range(N+2)]

    for i in range(len(ipt)-1):
        id1, x1, y1 = ipt[i]

        for j in range(i, len(ipt)):
            id2, x2, y2 = ipt[j]

            if abs(x2-x1)+abs(y2-y1) <= 1000 :
                adj[id1].append(id2)
                adj[id2].append(id1)


    # 2. bfs: 집 -> 페스티벌 갈 수 있는지 체크

    # [0] 초기 자료형
    v = [0]*(N+2)
    q = deque()

    # [1] 시작 위치
    v[0] = 1
    q.append(0)

    while q :
        c = q.popleft()

        # 종료 조건
        if c == N+1 :
            print('happy')
            break

        for n in adj[c] :
            if v[n] == 0 :
                v[n] = 1
                q.append(n)
    else :
        print('sad')
