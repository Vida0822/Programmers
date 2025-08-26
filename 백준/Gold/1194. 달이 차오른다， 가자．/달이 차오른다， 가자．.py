from collections import deque
key_map = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f'}
INF = ((50*50)**6)**6

def bfs(si, sj):

    # [0] 필요한 자료형
    q = deque()
    v = set()
    ans = INF

    # [1] 첫방문
    q.append((si, sj, '', 0)) # 열쇠 없음
    v.add((si, sj, ''))

    # [2] 순회
    while q:
        ci, cj, keys, cnt = q.popleft()

        if A[ci][cj] == str(1):
            ans = min(ans, cnt)
            continue

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci+di, cj+dj

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            # 벽
            if A[ni][nj] == '#':
                continue

            # 열쇠
            elif A[ni][nj] in ('a', 'b', 'c', 'd', 'e', 'f'):

                if A[ni][nj] not in keys:
                    # print(ni, nj, A[ni][nj])
                    new_keys = ''.join(sorted(keys+A[ni][nj]))
                    if (ni, nj, new_keys) not in v :
                        q.append((ni, nj, new_keys, cnt+1))
                        v.add((ni, nj, new_keys))
                else :
                    if (ni, nj, keys) not in v :
                        q.append((ni, nj, keys, cnt + 1))
                        v.add((ni, nj, keys))


            # 문
            elif A[ni][nj] in ('A', 'B', 'C', 'D', 'E', 'F'):
                if key_map[A[ni][nj]] not in keys:
                    continue
                if (ni, nj, keys) not in v :
                    q.append((ni, nj, keys, cnt+1))
                    v.add((ni, nj, keys))

            else : # 출구 or 길
                if (ni, nj, keys) not in v :
                    q.append((ni, nj, keys, cnt + 1))
                    v.add((ni, nj, keys))
            # print(q)
    return ans if ans != INF else -1


# [0] 준비
N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if A[i][j] == str(0):
            si, sj = i, j
            A[i][j] = '.'
            break

# [1] BFS
ANS = bfs(si, sj)

# [2] 정답
print(ANS)

