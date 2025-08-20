def check(ci, cj): # 주변 8칸이 지뢰가 없는 칸인지 확인하는 함수
    for di, dj in ((-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)):
        ni, nj = ci + di, cj + dj

        if not (0 <= ni < N and 0 <= nj < N):
            continue
        if adj[ni][nj] == '*': # 지뢰가 하나라도 있으면
            return False  # False 반환
    else:  # 그렇지 않으면
        return True # '0'인 칸이다


def bfs(si, sj):
    # *******여기서 문제 발생!*******
    # 주변 8칸을 표시할 때, 만약 '0'인 칸이 또 있다면 클릭 한번으로 재귀적으로 뻗어나가기에
    # 만약 주변에 '0'인 칸(즉 지뢰가 인접 8방향에 없는 칸)이 있다면 BFS로 포함해줘야함

    # [0] 필요한 자료형 + 첫방문
    q = [(si, sj)]
    v[si][sj] = 1

    # [1] 순회
    while q :
        ci, cj = q.pop(0)
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), # 8방향 조회하면서
                       (0, -1), (0, 1),
                       (1, -1), (1, 0), (1, 1)):
            ni, nj = ci + di, cj + dj

            if not (0 <= ni < N and 0 <= nj < N) : # 범위 밖이면 continue (default)
                continue

            if not v[ni][nj] and adj[ni][nj] == '.' : # 방문 안했고 지뢰가 없는 칸이면
                v[ni][nj] = 1  # 지뢰 개수 표시 (방문 표시로 대체: 0외에는 숫자를 표시해줄 필요 없음)
                if check(ni, nj):  # 그 인접 칸도 주변에 지뢰가 없는 '0'인 칸인지 확인해서
                    q.append((ni, nj)) # 새로운 BFS 시작점으로 포함


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    adj = [list(input()) for _ in range(N)]

    ANS = 0
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j] and adj[i][j] == '.': # 이미 조사한 좌표가 아니고 지뢰가 없는 자리일 때
                if check(i, j): # 주변에 지뢰가 하나도 없는 '0' 칸인지 확인
                    ANS += 1  # 클릭 수 증가
                    bfs(i, j) # 주변에 숫자 표시

    for i in range(N):
        for j in range(N):
            if not v[i][j] and adj[i][j] == '.': # 연쇄적으로 클릭되지 않는 지뢰 X 칸은
                ANS += 1 # 위에서 걸러졌다는건 주변에 지뢰가 있는 칸이라는 뜻이기 때문에 check, bfs 진행 X => 일일히 클릭해줘야함 
                v[i][j] = 1

    print(f'#{tc} {ANS}')
