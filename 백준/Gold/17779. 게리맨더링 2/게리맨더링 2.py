"""
핵심:
- 5번 구역: 마름모 처리 (규칙성) -> v 표시
- 1~4번 구역 : v 표시X 나머지 범위

=> TIP :
- 문제에 나와있는 수식은 그대로 활용하자
- 좌표가 복잡할 때는 그림으로 꼭 그려보자
- N이 작다 (20) -> 어렵게 생각하지 말고 완탐하자.

'마름모 형태가 바뀌는 코드 기억'
"""

# [0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

tot = sum(map(sum, arr))
ans = 100*N*N # 한 선거구가 모두 차지했을 때 최대값

# [1]
def cal(si, sj, d1, d2):
    v = [[0]*N for _ in range(N)]  # 5번 구역을 표시하기 위한 v 배열
    alst = [0]*5

    # [1] 5번 구역 표시(모두)
    v[si][sj] = 1
    j1 = j2 = sj
    for di in range(1, d1+d2+1):
        if di <= d1 : j1-=1  # 시작j(j1) 감소
        else: j1 +=1  # 시작j(j1) 증가

        if di <= d2 : j2+=1  # 시작j(j1) 감소
        else: j2 -=1  # 시작j(j1) 증가

        # 한번에 채워넣기!
        v[si+di][j1:j2+1] = [1]*(j2-j1+1)


    # [2] 1~4 구역 인구수(arr) 누적
    test = [[0]*N for _ in range(N)]
    for i in range(si+d1): # si+d1 미포함
        for j in range(sj+1): # sj 포함
            if v[i][j] == 1:
                break # 표시된건 5번 구역이므로 continue
            alst[0] += arr[i][j]
            # test[i][j] = 1
    for i in range(si+d2+1): # si+d2 포함
        for j in range(N-1, sj, -1): # sj 미포함
            if v[i][j] == 1:
                break
            alst[1] += arr[i][j]
            # test[i][j] = 2
    for i in range(N-1, si+d1-1, -1):  # si+d1 포함
        for j in range(sj-d1+d2): # sj-d1+d2 미포함
            if v[i][j] == 1:
                break
            alst[2] += arr[i][j]
            # test[i][j] = 3
    for i in range(N-1, si+d2, -1): # si+d2 미포함
        for j in range(N-1, sj-d1+d2-1, -1): # sj-d1+d2 포함
            if v[i][j] == 1:
                break
            alst[3] += arr[i][j]
            # test[i][j] = 4

    debug = 4
    alst[4] = tot-sum(alst)
    return max(alst)-min(alst)

# MAIN : Brute Force
# 모든 시작점 위치에서, 모든 (d1 & d2) 조합 구하기
for si in range(N-2):
    for sj in range(1, N-1):
        for d1 in range(1, N):
            # 범위 체크 : 4개 모두 좌표 계산하기 어려우니 2개정도는 범위 체크 형식으로 바꿔주기
            if 0 <= si+d1 < N and 0 <= sj-d1 < N :
                for d2 in range(1, N):
                    if 0 <= si+d1+d2 < N and sj+d2 < N: # d1, d2만큼 뻗어도 범위내이면
                        ans = min(ans, cal(si, sj, d1, d2)) # 문제는 무조건 top-down 설계

# [2]
print(ans)
