def dfs(n, scr, cal, cnt): # 검사 위치, 점수 합계, 포함 개수
    global ANS

    # 가지 치기
    if cal > L:
        return
        
    # [0] 종료 조건
    if n == N:
        ANS = max(ANS, scr)
        return

    # [1] 재귀 호출
    dfs(n+1, scr+ing[n][0], cal+ing[n][1], cnt+1)
    dfs(n+1, scr, cal, cnt)

T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())

    ing = [list(map(int, input().split())) for _ in range(N) ]
    ANS = 0
    dfs(0, 0, 0, 0)

    print(f'#{t} {ANS}')
