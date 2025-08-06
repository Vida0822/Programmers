from collections import deque

def bfs(si, sj, e):
    # [0] 필요한 자료형
    v = [[0]*11 for _ in range(3)]
    q = deque()

    # [1] 첫방문
    v[si][sj] = 1
    q.append((si, sj, 0))

    # [2] 인접 노드 탐색
    while q :
        ci, cj, t = q.popleft()

        for di, dj in ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1)):
            ni, nj = ci+di, cj+dj

            # 범위 검사
            if not (0 <= ni <= 2 and 0 <= nj < 10):
                continue

            # 방문 검사
            if v[ni][nj] == 0 and adj[ni][nj] != 0:
                v[ni][nj] = 1

                # 그래프 검사
                if adj[ni][nj] == e :
                    return ni, nj, t+3
                else :
                    q.append((ni, nj, t+2))
    else:
        return si, sj, 1


# 1. 그래프 만들기
adj = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
       ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',  0 ],
       ['Z', 'X', 'C', 'V', 'B', 'N', 'M',  0 ,  0 ,  0 ]]

T = int(input())
for _ in range(T) :
    S = input()
    ans = 1

    # 2 시작 문자 좌표 찾고
    s = S[0]
    for i in range(3):
        for j in range(10):
            if adj[i][j] == s:
                si, sj = i, j

    # 3. 문자열의 각 문자 읽으면서
    for e in S[1:]:

        # 4. 해당 문자 -> 다음 문자로 거리 구하기 (-> 시간 계산)
        ret = bfs(si, sj, e)
        ans += ret[2]

        # 5. 시작 문자 갱신
        si, sj = ret[0], ret[1]

    # 4. 답 출력
    print(ans)
