"""
크루스칼 알고리즘으로 풀이
=> 3차 제출 : 코드 열람 후 리펙토링
"""

from heapq import heappop, heappush, heapify

def find(n) :
    if P[n] != n :
        P[n] = find(P[n])
    return P[n]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        P[b] = a
    else:
        P[a] = b

TC = int(input())
for tc in range(1, TC+1):

    # 1. 그래프 만들기
    V, E = map(int, input().split())
    edges = []  # 간선 중 작은걸 계속 뽑아줘야하기 때문에 간선 정보를 담은 리스트 생성
    for _ in range(E):
        s, e, w = map(int, input().split())
        heappush(edges, (w, s, e))

    # 2. P 배열 정의
    P = [i for i in range(V+1)]

    # 3. 순회
    ANS = 0
    while edges:
        w, s, e = heappop(edges)

        if find(s) != find(e) :
            union(s, e)
            ANS += w

    print(f'#{tc} {ANS}')