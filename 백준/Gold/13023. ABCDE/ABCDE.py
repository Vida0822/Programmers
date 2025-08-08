import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dfs(n, i): # 검사 명수, 포함 순서, 포함 개수

    # [0] 종료 조건
    if n == 5:
        return 1

    # [1] 재귀 호출
    for j in adj[i]:
        if not v[j]:
            v[j] = 1
            if dfs(n+1, j): return 1
            v[j] = 0
    return 0


N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

v = [0]*N  # index가 0부터 시작
adj.append(0)
for i in range(N):
    if v[i] == 0:
        v[i] = 1
        if dfs(1, i):
            print(1)
            break
        v[i] = 0
else:
    print(0)