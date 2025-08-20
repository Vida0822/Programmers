"""
강사님 코드
: DFS

=> 이 아이디어는 생각했으나 시간 복잡도가 불안하여 하지 않음 (계산 자체를 못함)
=> 백트래킹 시간복잡도 정확히 알기
= 500*500*4*6*8 = 250000*200 = 5천만 < 10^8 + 가지치기
"""

def dfs(n, sm, loc): # n이 cnt 역할
    global ANS

    # 가지치기
    if sm + mx*(4-n) < ANS :
        return

    # [0] 종료조건
    if n == 4:
        ANS = max(ANS, sm)
        return

    # [1] 재귀호출
    for ci, cj in loc:
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci+di, cj+dj

            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] :
                v[ni][nj] = 1
                dfs(n+1, sm+arr[ni][nj], loc+[(ni, nj)])
                v[ni][nj] = 0







    pass
N, M = map(int, input().split())  # Refactoring: 앞에 두 값은 N과 M으로, 나머지는 rest 라는 리스트에 담김
arr = [list(map(int, input().split())) for _ in range(N)]
mx = max(map(max, arr))

ANS = 0
v = [[0]*M for _ in range(N)]
for i in range(N) : # 500
    for j in range(M) :
        v[i][j] = 1
        dfs(1, arr[i][j] , [(i, j)])

print(ANS)