from heapq import heappush, heappop, heapify
from collections import deque

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    ipts = list(map(int, input().split()))
    q = deque()
    hq = []
    for i in range(N):
        q.append((i, ipts[i]))
        heappush(hq, -ipts[i])

    i = 0
    while hq:
        n = -heappop(hq)
        i += 1
        while q[0][1] != n:
            q.append(q.popleft())
        else:
            if q[0][0] == M :
                break
            q.popleft()
    print(i)
