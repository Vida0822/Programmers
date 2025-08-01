def q_atteck(si, sj) :
    # 8 방향 , while문 조건 --> 장애물
    v[si][sj] = 1

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, 1), (-1, -1)) :
        ni, nj = si+di, sj+dj

        while 1 <= ni < N+1 and 1 <= nj < M+1 and arr[ni][nj] == 0:
            v[ni][nj] = 1
            ni += di
            nj += dj

def k_atttack(si, sj) :
    v[si][sj] = 1

    # 8방향, 장애물 상관 X
    for di, dj in ((-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2)) :
        ni, nj = si + di, sj + dj

        if 1 <= ni < N + 1 and 1 <= nj < M + 1:
            v[ni][nj] = 1
        # while 1 <= ni < N + 1 and 1 <= nj < M + 1:
        #     v[ni][nj] = 1
        #     ni += di
        #     nj += dj


# 1. 그래프 만들기
N, M = map(int, input().split())
arr = [[0]*(M+1) for _ in range(N+1)]

Q_ipt = list(map(int, input().split()))
q = Q_ipt.pop(0)
if q != 0 :
    for i in range(0,q*2,2):
        arr[Q_ipt[i]][Q_ipt[i+1]] = 'Q'

K_ipt = list(map(int, input().split()))
k = K_ipt.pop(0)
if k != 0 :
    for i in range(0,k*2,2):
        arr[K_ipt[i]][K_ipt[i+1]] = 'K'

P_ipt = list(map(int, input().split()))
p = P_ipt.pop(0)
if p != 0 :
    for i in range(0,p*2,2):
        arr[P_ipt[i]][P_ipt[i+1]] = 'P'
        # print(P_ipt[i], P_ipt[i+1])
# for a in arr :
#     print(*a)

# 2. 전체 좌표 순회
v =  [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1) :
    for j in range(1, M+1):
        if arr[i][j] == 'Q':
            q_atteck(i, j)
        elif arr[i][j] == 'K' :
            k_atttack(i, j)
        elif arr[i][j] == 'P' :
            v[i][j] = 1

# 3. 안전 지역 계산
ans = 0
for i in range(1, N+1) :
    for j in range(1, M+1):
        if v[i][j] == 0 :
            ans += 1
#
# for vv in v :
#     print(*vv)

print(ans)