"""
최소 신장 트리 : 인접 행렬 그래프 ver
=> 템플릿에서 인접 노드 조회하는 부분만 수정
: 해당 행의 다른 열로의 이동

"""

def find(n):
    if n != P[n] :
        P[n] = find(P[n])  # 경로 압축
    return P[n]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b :
        P[b] = a
    else :
        P[a] = b

def Kruscal(edges):

    # [0] 필요한 자료형
    ANS = 0

    # [1] 가중치 합 구하기
    while edges: # O(N^2//2)
        w, s, e = heappop(edges)

        if find(s) != find(e):
            union(s, e)
            ANS += w

    return ANS


from heapq import heappush, heappop

# 1. 그래프 만들기
N = int(input())
edges = []
for s in range(N): # O(N^2)
    ends = list(map(int, input().split()))
    for e in range(s+1, len(ends)): # refactoring
        heappush(edges, (ends[e], s+1, e+1))

# 2. 크루스칼 알고리즘
P = [i for i in range(N+1)] # O(N)
print(Kruscal(edges))

