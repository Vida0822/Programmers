"""
1차 시도 : 시간 초과 -> memo 사용 ?

"""
from collections import deque

def bfs(s) :
    # [0] 필요한 자료형 준비
    v = set()
    cnt = 0
    q = deque()

    # [1] 시작 위치 반영
    v.add(s)
    cnt += 1
    q.append(s)

    while q :
        c = q.popleft()

        for n in adj[c] :
            if n not in v :
                if memo[s] != 0 :
                    cnt += memo[s]
                    continue
                v.add(n)
                cnt += 1
                q.append(n)

    memo[s] = cnt
    return cnt


# 1. 그래프 만들기
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
memo = [0]*(N+1)

for _ in range(M) :
    A, B = map(int, input().split())
    adj[B].append(A) # 방향그래프

ans = [0]
cnt = 0
for i in range(1, N+1):
    if memo[i] != 0 :
        com = memo[i]
    else :
        com = bfs(i)
    if cnt < com :
        ans = [i]
        cnt = com
    elif cnt == com :
        ans.append(i)

print(*sorted(ans))
