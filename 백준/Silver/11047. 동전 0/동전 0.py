"""
그리디 keypoint
1. 반례
2. 정렬
"""

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)] # 이미 정렬되어있음

ANS = 0
for i in range(N-1, -1, -1):
    ANS += K//A[i]
    K %= A[i]

print(ANS)


