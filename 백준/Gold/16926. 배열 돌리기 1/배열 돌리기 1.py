def test():
    for a in A:
        print(*a)
    print()

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K = min(N, M) // 2

def rotate():
    for k in range(K) :
        si, sj = k, k
        ei, ej = N-1-k, M-1-k

        t = A[si][ej]

        # 1. 오른쪽 끝열 ↑
        for i in range(si+1, ei+1):
            A[i-1][ej] = A[i][ej]
        # debug = 0
        # test()

        # 2. 맨 아래 끝행 →
        for j in range(ej-1, sj-1, -1):
            A[ei][j+1] = A[ei][j]
        # debug = 1
        # test()

        # 3. 왼쪽 끝열 ↓
        for i in range(ei-1, si-1, -1):
            A[i+1][sj] = A[i][sj]
        # debug = 2
        # test()

        # 4. 맨 위 첫 행 ←
        for j in range(sj+1, ej):
            A[si][j-1] = A[si][j]
        A[si][ej-1] = t
        # debug = 3
        # test()

for _ in range(R) :
    rotate()
    # test()

for a in A:
    print(*a)