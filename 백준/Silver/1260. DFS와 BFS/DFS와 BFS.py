def dfs(c) :
    # 1. 방문
    v[c] = 1
    ans.append(c)

    # 2. 인접 노드
    for n in adj[c] :
        if v[n] == 0 :
            dfs(n)


def bfs(s) :
    # 1. 초기화
    v = [0]*(N+1)
    ans = []
    q = []

    # 2. 첫방문
    v[s] = 1
    ans.append(s)
    q.append(s)

    while q:
        c = q.pop(0)

        for l in adj[c] :
            if v[l] == 0 :
                v[l] = 1 # 0 --> 이거 계속 실수 ㅠㅠ
                ans.append(l)
                q.append(l)

    return ans

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M) :
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for lst in adj :
    lst.sort()

# 1. 초기화
# dfs
v = [0]*(N+1) # [[0] for _ in range(N+1)] --> 이렇게하면 2차원 배열!! 0이 하나씩 들어있는
ans = []
dfs(V)
print(*ans)

# bfs
print(*bfs(V))


