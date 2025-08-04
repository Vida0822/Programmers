import sys
sys.setrecursionlimit(100000)

def dfs(c):
    # 첫방문 시 해야할 일
    # 종료 조건
    # 4방향/8방향/연결된..반복처리
    for n in adj[c]:
        if v[n] == 0 :
            v[n] = c
            dfs(n)

# 1. 그래프 만들기
N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

# 2. 루트 노드부더 dfs : 자연히 부모 -> 자식 순으로 방문
v = [0]*(N+1) # 방문 배열에 자신의 부모 노드
dfs(1)
print('\n'.join(map(str, v[2:])))
