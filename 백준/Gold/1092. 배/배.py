"""
조건 : N <= 50
"""

def solve():
    N = int(input())
    C = list(map(int, input().split()))# 크레인
    C.sort(reverse=True)

    M = int(input())
    W = list(map(int, input().split())) # 화물
    W.sort(reverse=True)

    ANS = 0
    if C[0] < W[0]:
        ANS = -1
    else:
        while W: # 화물이 남아있으면
            ANS += 1 # 시간 추가
            for c in C:  # 크레인하나씩 보면서
                if W and c < W[-1] : continue  # 가장 가벼운게 현재 크레인 가능 용량보다 크면 검사 X
                for w in W:
                    if c >= w : # 크레인이 적재할 수 있다면 (debug: 같거나 크다)
                        W.remove(w) # 짐 삭제
                        break
    return ANS






print(solve())
