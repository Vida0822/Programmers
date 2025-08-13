"""
최소 신장 트리
1. Prim: 현재 위치한 노드에서 가장 작은 가중치로 이동할 수 있는 노드 pop
2. Kruscal: 가중치가 가장 작은 간선을 뽑아내서 같은 집합이 아니라면 inn

이 문제: 음수 가중치는 포함해도 되나, 음수 사이클은 만들면 안된다!
"""
from heapq import heappop, heappush, heapify
import sys
sys.setrecursionlimit(100000)


def find(n):
    if n != P[n]:
        P[n] = find(P[n])
    return P[n]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b :
        P[b] = a
    else :
        P[a] = b

# 1. Kruscal
def Kruscal(edges):

    heapify(edges)
    ANS = 0

    while edges:
        w, s, e = heappop(edges)
        if find(s) != find(e):
            union(s, e)
            ANS += w

    return ANS



# 1. 그래프 만들기
V, E = map(int, input().split())

edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))


# 2. 신장트리 만들기
P = [0]+[i for i in range(1, V+1)]
print(Kruscal(edges))
