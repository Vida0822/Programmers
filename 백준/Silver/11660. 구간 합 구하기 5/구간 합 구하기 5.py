"""
조건
N = 10^3 , M = 10^6
--> 완전 탐색: 10^9 (시간 초과)

=> 누적합 배열 사용
1. 누적합 배열 만들기 --> O(N^2)
2. 누적합 구하기 --> O(M*N)

"""
N, M = map(int, input().split())
A = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# 1. 누적합 배열 구하기
SUM = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1) :
    for j in range(1, N+1):
        SUM[i][j] = SUM[i][j-1]+A[i][j]
# for sum in SUM:
#     print(*sum)

# 2. 누적합 구하기
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    sm = 0
    for cx in range(x1, x2+1) :
        sm += SUM[cx][y2] - SUM[cx][y1-1]

    print(sm)
