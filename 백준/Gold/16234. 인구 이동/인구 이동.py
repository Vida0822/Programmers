from collections import deque

# BFS
def bfs(si, sj):
    # [0] 필요한 자료형
    ans = []
    sm = 0
    q = deque()

    # [1] 첫방문
    sm += A[si][sj]
    ans.append((si, sj))
    v[si][sj] = 1
    q.append((si, sj))

    # [2] 순회
    while q:
        ci, cj = q.popleft()

        # 인접 조회
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj

            # 범위
            if not (0 <= ni < N and 0 <= nj < N):
                continue

            # 미방문 & 조건
            if not v[ni][nj] and (L <= abs(A[ci][cj]-A[ni][nj]) <= R):
                # 정답 처리
                sm += A[ni][nj]
                ans.append((ni, nj))
                
                # 다음 방문 준비
                v[ni][nj] = 1
                q.append((ni, nj))
    return ans, sm

# MOVE
def move():

    for union in unions:
        members = union[0]
        sm = union[1]
        cnt = len(members)
        for ci, cj in members:
            # print(members)
            A[ci][cj] = int(sm/cnt)



# MAIN
# [0] 필요한 자료형
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True :
    v = [[0]*N for _ in range(N)]
    unions = []

    # 1. 국경선 open (연합 만들기)
    for i in range(N):
        for j in range(N) :
            if not v[i][j]:
                union = bfs(i, j)
                if len(union[0]) > 1 :
                    unions.append(union)

    # 2. 인구 이동
    if unions:
        # print(unions)
        move()
    else:
        break
    #
    # for a in A:
    #     print(*a)
    # print()
    ans += 1


# 3. 정답 출력
print(ans)


