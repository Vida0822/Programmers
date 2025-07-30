def bfs(s, g) :
    # 초기화
    v = [0]*(N+1)
    v[s] = 1
    q = [s]

    while q :
        c = q.pop(0)

        for n in adj[c] :
            if n == g :
                return v[c]

            if v[n] == 0 : # 방문 x
                v[n] = v[c] + 1
                q.append(n)
    else :
        return -1

# 1. 그래프 만들기
N = int(input())
S, G = map(int, input().split())
E = int(input())

# 양방향 그래프 : 부모, 자식 상관없이 이어져있는(1촌관계)인 요소들
adj = [[] for _ in range(N+1)] # debug : 요소 하나 더만드는거 계속 까먹음...
for _ in range(E) :
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# 2. 탐색
print(bfs(S, G))
