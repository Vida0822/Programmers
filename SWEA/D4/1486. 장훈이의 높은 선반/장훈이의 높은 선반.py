"""
선택/선택 X로 풀어봄
"""
def dfs(n, sm): # n = n번째 직원
    # [0] 종료 조건
    global S

    if n == N:  # 직원 전원을 다 검사했을 때
        if sm >= B: # 정답 조건
            S = min(S, sm)
        return

    # [1] 재귀 호출
    dfs(n+1, sm+H[n]) # 해당 직원을 포함한 조합 만들기
    dfs(n+1, sm) # 해당 직원을 포함하지 않은 조합 만들기 (어쨌든 검사 위치는 다음 직원으로 이동)


T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    S = 10000*20
    dfs(0, 0)

    print(f'#{t} {S-B}')
