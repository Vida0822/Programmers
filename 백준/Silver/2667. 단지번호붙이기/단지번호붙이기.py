def bfs(si, sj, idx) :
    # 초기화
    v[si][sj] = 1
    ans.append(1)
    q = [(si, sj)]

    while q :
        ci, cj = q.pop(0)
        # 종료 조건
        # X

        # 인접 노드 방문
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci+di, cj+dj

            # 범위 체크
            if not (0 <= ni < N and 0 <= nj < N) :
                continue

            # 조사
            if adj[ni][nj] == 1 and v[ni][nj] == 0 :
                v[ni][nj] = 1
                ans[-1] = ans[-1] + 1 # ans 반영은 여기서 하면 좋음!
                adj[ni][nj] = idx
                q.append((ni, nj)) # debug : list.append() takes exactly one argument (2 given)


N = int(input())
adj = [list(map(int, input())) for _ in range(N)]
v = [[0]*N for _ in range(N)]

ans = []
idx = 2
for i in range(N) :
    for j in range(N) :
        if adj[i][j] == 1 and v[i][j] == 0 :
            adj[i][j] = idx
            bfs(i, j, idx)  # 원래 있던 1과 헷갈릴 수 있기 때문에 새롭게 부여한 인덱스는 2부터 시작 (실제로 인덱스를 출력할 일이 없기 때문에)
            idx += 1 # debug : 인덱스를 업데이트를 안해줘서 계속 1이 들어감 --> 중복 검사 (1이면 검사한다고 bfs에서 설정해서... )

ans.sort() # debug...이거 까먹음 ㅠㅠ
print(len(ans))
print(*ans, sep = '\n')
