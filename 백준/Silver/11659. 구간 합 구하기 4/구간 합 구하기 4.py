"""
1차 시도 : 완전 탐색 --> 시간 초과 실패
2차 시도 : 투포인터 --> 실패..
3차 시도 : 수학

[조건]
양 끝(i, j)를 포함하는 구간합

[구상]
a~b의 구간합 = a까지의 구간합 + a-1까지의 구간합
"""
N, M = map(int, input().split())
A = [0]+list(map(int, input().split()))

SUM = [0]*(N+1)

for i in range(1, N+1): # O(N)
    SUM[i] = SUM[i-1] + A[i]

for _ in range(M):
    ni, nj = map(int, input().split())
    print(SUM[nj] - SUM[ni-1])

