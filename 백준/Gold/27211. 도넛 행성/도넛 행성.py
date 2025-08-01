from collections import deque

def bfs(si, sj) :
    # [0] 필요한 자료형
    q = deque()

    # [1] 시작 위치
    v[si][sj] = 1
    q.append((si, sj))

    # [2] 구역 내 좌표 찾기
    while q :
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni,nj = (ci+di)%N, (cj+dj)%M

            if v[ni][nj] == 0 and adj[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj))

# 1. 그래프 만들기
N, M = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(N)]

v = [[0]*M for _ in range(N)]
ans = 0
# 2. 전체 좌표 순회
for i in range(N):
    for j in range(M) :
        # 3. 갈수 있는 구역 표시하기 
        if v[i][j] == 0 and adj[i][j] == 0 :
            bfs(i, j)
            ans += 1

print(ans)


