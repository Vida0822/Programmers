def solve():
    # [0]
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # [1] BFS
    # [0]
    v = set()
    alive = set()
    q = []

    # [1]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                q.append((i, j, arr[i][j], 0))
                alive.add((i, j))
                v.add((i, j))

    # [2]
    debug = 1
    for t in range(K):
        nq = []
        q.sort(key=lambda x: (-x[2]))
        while q:
            ci, cj, x, age = q.pop(0)

            if 2*x <= age: # 죽은 상태
                alive.remove((ci, cj))
            else:
                if x <= age: # 활성상태
                    for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                        ni, nj = ci+di, cj+dj

                        if (ni, nj) in v:
                            continue

                        nq.append((ni, nj, x, 0))
                        alive.add((ni, nj))
                        v.add((ni, nj))
                nq.append((ci, cj, x, age+1))
        q = nq

    while q:
        ci, cj, x, age = q.pop(0)
        if 2 * x <= age:  # 죽은 상태
            alive.remove((ci, cj))

    # [2]
    # print(alive)
    return len(alive)

#############################################3
TC = int(input())
for tc in range(1, TC+1):
    ANS = solve()
    print(f'#{tc} {ANS}')