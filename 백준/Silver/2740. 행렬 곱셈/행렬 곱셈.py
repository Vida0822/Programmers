# 1. 입력
N, M = map(int, input().split()) # A 행렬
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())  # B행렬
B = [list(map(int, input().split())) for _ in range(M)]

# 2. 행렬의 곱 = 앞행렬의 행에 뒷행열의열을 곱한다 --> 개수가 맞는 쪽을 기준
arr = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        sm = 0
        for k in range(M):
            sm += A[i][k]*B[k][j]
            # print(A[i][k]*B[k][j])
        arr[i][j] = sm

# 3. 답 출력
for a in arr:
    print(*a)

