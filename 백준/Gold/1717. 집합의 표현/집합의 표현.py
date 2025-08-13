import sys
sys.setrecursionlimit(100000)

def find(n) :
    if n != P[n] :
        P[n] = find(P[n]) # 경로 압축
    return P[n]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b :
        P[b] = a
    else:
        P[a] = b

n, m = map(int, input().split())
P = [i for i in range(0, n+1)]
for _ in range(m) :
    ord, a, b = map(int, input().split())

    if ord == 0 :
        union(a, b)
    else :
        if find(a) == find(b) :
            print('YES')
        else :
            print('NO')
