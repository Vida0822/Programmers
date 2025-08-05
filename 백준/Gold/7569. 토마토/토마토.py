"""
1차 풀이) 실패
2차 풀이) 풀이 시간 : 30분 (구상 10분, 구현 10분, 디버깅 10분)

[배운점]
1. 히든 케이스가 안풀릴 땐 부분 고치는게 아닌 구상 자체를 점검해야함
2. 안풀릴 땐 그 문제만 계속 붙잡는게 아닌 일단 넘어가거나, 리프레쉬, 구상 재설계 **
"""
from collections import deque
def solve():

    # 1. 그래프 만들기
    M, N, H = map(int, input().split())
    adj = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    # 2. 좌표 검사하면서 익은 토마토 확인
    q = deque()
    v = [[[0]*M for _ in range(N)] for _ in range(H)]
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if adj[h][i][j] == 1:
                    q.append((h, i, j, 0))  # d = 0
                    v[h][i][j] = 1
                    # debug: bfs 할 때 인접노드 방문할 때만 방문표시하기에 큐에 넣을 때 안해주면 무한루프 (계속 재방문 : 그래프가 0일 때만 방문 처리하므로)

                    # ans = max(bfs(h, i, j, 0), adj[h][i][j])
                    # 이렇게 하면 X : 토마토 칸이 분리되어있는데서 각각 익히는게 아닌 대부분 연결되어있는 통로인데
                    # 한 지점에서 bfs하면 그 이전에 다른 지점에서 익는 토마토가 다른 일자에 익히게 되고
                    # 다음 익은 토마토 검사할 때도 오류가 나타나게됨
                    # 익은 토마토가 있다면, 검사할 큐로 먼저 삽입하고 차례로 꺼내서 익혀야함 (날짜별로)


    # 3. bfs
    d = -1
    while q:
        ch, ci, cj, d = q.popleft()
        # print(ch, ci, cj, d)
        # print(v[ch][ci][cj])

        # 인접 노드 방문
        for dh, di, dj in ((1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            nh, ni, nj = ch+dh, ci+di, cj+dj

            # 조건 1 : 범위
            if not (0 <= nh < H and 0 <= ni < N and 0 <= nj < M):
                continue

            # 조건 2 : 방문 X & 안익은 토마토
            if v[nh][ni][nj] == 0 and adj[nh][ni][nj] == 0:
                # adj[nh][ni][nj] == 1 # 그래프 수정  # debug : 또..또 '==' 썼다
                adj[nh][ni][nj] = 1
                # v[nh][ni][nj] == 1 # 방문 처리
                v[nh][ni][nj] = 1
                q.append((nh, ni, nj, d+1))  # 큐 삽입


    for h in range(H):
        for i in range(N):
            for j in range(M):
                if adj[h][i][j] == 0 :
                   return -1
    else :
        return d


print(solve())