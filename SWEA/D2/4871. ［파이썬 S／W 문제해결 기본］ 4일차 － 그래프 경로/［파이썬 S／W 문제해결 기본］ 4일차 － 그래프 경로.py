def dfs_stack(S, G) :
    # 필요한 자료형
    v = [0]*(V+1)
    ans = []
    stk = []

    # 첫방문
    c = S
    v[c] = 1
    ans.append(c)

    # 방문 시작
    while True :
        for n in graph[c] :
            if v[n] == 0 :
                c = n
                stk.append(c)
                v[c] = 1
                break
        else :
            if stk:
                c = stk.pop()
            else:
                break
    return v[G]


T = int(input())
for t in range(1, T+1):

    # 그래프 만들기
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E) :
        s, e = map(int, input().split())
        graph[s].append(e) # 방향 그래프

    S, G = map(int, input().split())

    print(f'#{t}',dfs_stack(S, G))
