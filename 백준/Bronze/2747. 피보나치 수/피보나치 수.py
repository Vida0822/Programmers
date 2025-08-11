"""
DP 기본 문제
1. top-down : 재귀호출+memo --> O(?)
2. bottom-up : 반복문 채워나가기 --> O(N^2) ?
"""

# 1. top-down
N = int(input())
dp1 = [0]*(N+1) # 10번째 피보나치 = 배열상 11번째의 수 

def fivo(n) :

    # [0] 종료 조건
    if n == 0 or n == 1 : 
        return n
    # else : 
    #     재귀호출
    
    # [1] 재귀 호출
    if dp1[n] == 0:
        dp1[n] = fivo(n-1)+fivo(n-2)

    return dp1[n]

# print(fivo(N-1)) # debug : list index out of range
print(fivo(N))

# 2. bottom-up