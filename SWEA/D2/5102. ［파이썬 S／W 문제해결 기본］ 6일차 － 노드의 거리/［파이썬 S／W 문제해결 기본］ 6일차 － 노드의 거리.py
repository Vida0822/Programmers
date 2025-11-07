"""
12:08 ~
"""

def bfs(s) :
    # 초기화
    v[s] = 0
    q = [s]

    while q :
        c = q.pop(0)

        for n in adj[c] :
            if v[n] == 0 :
                v[n] = v[c] + 1
                q.append(n)


T = int(input())
for tc in range(1, T+1) :

    # 1. 그래프 만들기
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]

    for _ in range(E) :
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    # 2. 탐색 시작
    S, G = map(int, input().split())
    v = [0]*(V+1) # debug
    bfs(S)
    print(f'#{tc} {v[G]}')