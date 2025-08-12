from heapq import heappush, heapify, heappop

N = int(input())
hq = [int(input()) for _ in range(N)]

heapify(hq)

ANS = cnt = sm = 0
while hq:
    sm += heappop(hq)
    if cnt == 0 :
        cnt += 1
    else:
        ANS += sm
        heappush(hq, sm)
        sm = cnt = 0
print(ANS)