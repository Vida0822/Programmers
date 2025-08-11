"""
디버깅 실패 -> 해답 참조

TIP: 안된다고 if문 여기저기 넣으면서 제출하기 절대 X
--> 1. 무조건 손코딩 로직 점검하고 (5분 이상)
--> 2. Edge Case 고려해서 구상 점검

"""

N = int(input())
A = [int(input()) for _ in range(N)]

# [0] table 정의
# dp[i] : A[i] 를 밟았을 때 얻을 수 있는 점수 최대값
dp = [0]*N


if len(A) <= 2 :
    print(sum(A))
else :
    # [1] 초기값
    dp[0] = A[0]
    dp[1] = A[0] + A[1]

    # [2] 점화식
    # for i in range(2, N+1):
    #     if dp[i-1] > dp[i-2] and cnt < 2:
    #         dp[i] = dp[i-1]+A[i]
    #         cnt += 1
    #     else : # dp[i-1] <= dp[i-2] or cnt > 3:
    #         dp[i] = dp[i-2]+A[i]
    #         cnt = 1
    # => FAIL : 이렇게 하면 dp[i-1]에 dp[i-2]를 선택한 경우의 수도 포함됨 (중복 계산됨)
    #       --> 3연속 계단 횟수 포함
    for i in range(2, N):
        dp[i] = max(dp[i-2]+A[i], dp[i-3]+A[i-1]+A[i])
    # 1) dp[i-2]+A[i] : 2칸 전 계단까지의 점수합 + 현재 계단 점수
    # 2) dp[i-3]+A[i-1]+A[i] : 3칸전 계단까지의 점수합 + 전 계단 점수 + 현재 계단 점수

    # [3] 정답 출력
    # print(dp)
    print(dp[-1])
