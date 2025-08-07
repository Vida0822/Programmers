"""
Refactoring : 전선택과 전전선택을 재귀함수의 인자로 넘겨줌 (계속 업데이트)
"""

def dfs(n, scr, bbv, bv):
    global ANS

    # 가지치기 : 남은 문제(총문제-푼문제)+현재점수 < 5 --> 고려할 필요 X
    if 10 - n + scr < 5:
        return

    # [0] 종료조건
    if n == N:
        # print(v)
        # if scr >= 5 : --> 위에서 가지치기해줬기때문에 5점 넘는지 확인할 필요 X
        ANS += 1 # 정답 처리
        return

    # [1] 재귀호출
    for j in range(1, 6):
        if j == bv and j == bbv : continue
        dfs(n+1, scr+int(A[n] == j), bv, j)

A = list(map(int, input().split()))
N = len(A)
ANS = 0

# v = [0]*6
dfs(0, 0, 0, 0)
print(ANS)
