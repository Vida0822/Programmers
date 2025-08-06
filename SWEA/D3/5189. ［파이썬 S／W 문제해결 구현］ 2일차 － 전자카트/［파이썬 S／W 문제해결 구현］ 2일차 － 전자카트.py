def dfs(n, i, sm, v): # 검사 위치, 이전 구역, 점수 합계, 포함 개수
    global ANS

    # 가지 치기
    if sm >= ANS:
        return

    # [0] 종료 조건
    if n == N-1: # debug : N->N-1 ) 사무실은 구역에서 제외되므로 최종 목표 구역 개수에서 빼줘야한다. 
        ANS = min(ANS, sm+bat[i][0])
        return

    # [1] 재귀 호출
    for j in range(1, N):
        if v[j] == 0:
            # print(bat[i][j])
            v[j] = 1
            dfs(n+1, j, sm+bat[i][j], v)
            v[j] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    bat = [list(map(int, input().split())) for _ in range(N)]

    ANS = 100*N # N? N**2?
    dfs(0, 0, 0, [0]*(N+1))

    print(f'#{t} {ANS}')
