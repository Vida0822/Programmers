"""
[접근]
: 부분 집합
ㄴ--> 단, 다음 요소를 확인할 때 직전 상담 소요일이 지난 후 : n+T 의 요소 확인

[조건]
상담 가능일 : 0 ~ N-1 => 상담 종료일 : 1 ~ N 
※ 마지막 날도 상담 가능함 주의


"""
def dfs(n, sm):
    global ANS

    # [0] 종료 조건
    if n == N:
        if ANS < sm :
            ANS = sm 
        return

    # [1] 재귀 호출
    dfs(n + 1, sm)  # n일 상담 X
    if n+mrg[n][0] <= N: # debug : 마지막 날 상담 소요시간이 1일이면 가능하기때문에 N도 포함해야함
        dfs(n+mrg[n][0], sm+mrg[n][1]) # n일 상담 o -> T[n] 일 후 가능



N = int(input())
mrg = [tuple(map(int, input().split())) for _ in range(N)]
ANS = 0
dfs(0, 0)

print(ANS)

