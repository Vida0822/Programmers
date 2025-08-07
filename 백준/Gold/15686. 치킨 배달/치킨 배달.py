"""
접근 : 백트래킹
조건 : N <= 50 , M <= 치킨집 <= 13
--> O(13^13) : 치킨집의 조합을 구하는 것이므로 --> ㄱㅊ!

"""

def cal_dist(ans):
    sm = 0  # 도시의 치킨 거리
    # 집의 치킨 거리
    for h in houses : # 각 집별로
        min_dist = 50*50+1
         #for ch in chickens :   --> debug : 이렇게 하면 모든 치킨집으로의 거리 구함
        #       => debuging 팁 : 인자를 제대로 사용하고 있는지 확인 --> 실수 多
        for ch in ans : # 해당 조합의 치킨집로의 거리를 구하고
            min_dist = min(min_dist, abs(h[0] - ch[0]) + abs(h[1] - ch[1]) ) # 그중 최소값이 집의 치킨 거리
        sm += min_dist # 각 집의 치킨거리를 도시 거리에 반영

    return sm


def dfs(n, i, ans):  # 검사 개수, 직전 선택(치킨집), 조합 구성(치킨집)
    global ANS
    # 가지 치기 : '집의 개수는 2N개를 넘지 않는다?'

    # [0] 종료조건
    if n == M:
        # print(ans)
        ANS = min(ANS, cal_dist(ans))   # 합계 반환 --> 최소값 갱신
        return

    for j in range(i+1, len(chickens)) :
        ans.append(chickens[j])
        dfs(n+1, j, ans)
        ans.pop()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))
        # else :   # 빈집
        #     pass

ANS = 50*50+1
dfs(0, -1, [])
print(ANS)