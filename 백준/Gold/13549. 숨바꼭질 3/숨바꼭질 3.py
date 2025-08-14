from collections import deque

def bfs(S, E) :
    global ANS

    # [0] 필요한 자료형
    q = deque()
    v = [100000]*100001

    # [1] 첫방문
    q.append((S, 0))
    v[S] = 0  # debug : 0 -> S

    # [2] 순회
    while q:
        # ct, cx = heappop(q)
        cx, ct = q.popleft()
        if v[cx] < ct:
            continue

        for dx, dt in ((-1, 1), (1, 1), (cx, 0)):
            nx, nt = cx+dx, ct+dt

            # 범위 확인
            if not (0 <= nx <= 100000):
                continue

            # 미방문 확인
            if 0 <= nx <= 100000 and v[nx] > nt:
                v[nx] = nt
                q.append((nx, v[nx]))

    return v[E]

S , E = map(int, input().split())
print(bfs(S, E))
