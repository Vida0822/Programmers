from heapq import heappush, heappop

N, M = map(int, input().split())
A = {}

# 1. 각 초밥 종류 별 원하는 손님 저장 (heapq)
for i in range(N) :
    types = list(map(int, input().split()))
    k = types.pop(0)

    for t in types:
        hq = A.get(t, [])
        heappush(hq, i)
        A[t] = hq

# print(A)

# 2. 만들어진 초밥 종류별 1순위 손님 반환
ANS = [0]*N
B = list(map(int, input().split()))
for t in B:
    if t in A and A[t] :
        i = heappop(A[t])
        ANS[i] += 1

print(*ANS)

