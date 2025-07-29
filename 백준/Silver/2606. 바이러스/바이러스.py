def dfs(c) :
    v[c] = 1

    for n in graph[c] :
        if v[n] == 0 :
            dfs(n)


# 그래프 만들기 (입력)
V = int(input())
E = int(input())

import sys
sys.setrecursionlimit(10000)

graph = [[] for _ in range(V+1)]
for _ in range(E) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

v = [0]*(V+1)
dfs(1)
print(v[2:].count(1))

