"""
[조건]
1 <= 점수 <= 100
 --> 차이 최대값 100*(N//2)

[구상]
조합 : 직전 방문 위치(i) 필요

N명 중 N//2 명 을 뽑는 조합 --> 해당 조합 내 선수 구성원으로 시너지 점수 계산
1. N//2 명으로 팀 구성  (종료조건: n == N//2)
2. 점수 구하기 : scr[i][j] + scr[j][i] (※ 양방향으로 구해야함)
3. 상대팀 점수 구하기
4. 두 팀 점수차 --> max값 갱신

* 방문 배열 사용 : 순열 만들기 위한 것이 아닌 team1에 포함되는 선수를 표시하기 위함

=> dfs(n, i, v) 
"""

def cal(team) :
    sm = 0
    for p1 in range(K-1):
        for p2 in range(p1+1, K) :
            sm += scr[team[p1]][team[p2]] + scr[team[p2]][team[p1]]
    return sm

def dfs(n, i, v):
    global ANS_MIN

    # [0] 종료 조건
    if n == K:
        # 정답 처리
        team1 = []
        team2 = []
        for i in range(1, N + 1):
            if v[i] == 1:
                team1.append(i)
            else:
                team2.append(i)
        # print(team1, team2, cal(team1), cal(team2))
        ANS_MIN = min(ANS_MIN, abs(cal(team1)-cal(team2)))
        return

    # [1] 재귀 호출
    for j in range(i+1, N+1):
        v[j] = 1 # team 1 에 소속되는 선수 표시 위함 (나중에 포함되지 않는 상대팀 점수도 구해야하므로)
        dfs(n+1, j, v)
        v[j] = 0


N = int(input())
K = N//2 # 한팀에 소속될 선수 명수 (집합을 만들 기준 명수)
scr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
# 패딩: 문제에 맞춰 1번부터 선수 인덱싱하기 위함

ANS_MIN = 100*(N//2)
dfs(0, 0, [0]*(N+1))
print(ANS_MIN)


