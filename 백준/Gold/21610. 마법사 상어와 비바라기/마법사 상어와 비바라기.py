from collections import deque

# [0] 시뮬레이션 준비
N, M = map(int , input().split())
A = [[0]*(N+1)]+[[0] + list(map(int, input().split())) for _ in range(N)]

q = deque([(N, 1), (N, 2), (N-1, 1), (N-1, 2)])
#  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
delta = {1:(0, -1) , 2:(-1, -1), 3:(-1, 0), 4:(-1, 1),
         5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}

# [1] 시뮬레이션 실행
for _ in range(M):
    d, s = map(int, input().split())
    di, dj = delta[d][0]*s, delta[d][1]*s

    # step1. 구름 이동
    nq = deque()
    while q:
        ci, cj = q.popleft()
        ni = (ci+di)%N if (ci+di)%N != 0 else N
        nj = (cj+dj)%N if (cj+dj)%N != 0 else N
        nq.append((ni, nj))

        # step2 : 물의 양 1증가
        A[ni][nj] += 1

    # 2. 물 증가
    v = set()
    while nq:
        ci, cj = nq.popleft()

        # step3 구름 사라짐 (있었음은 표시)
        v.add((ci, cj))
        
        # step4: 물복사버그
        cnt = 0
        # cp_A = [lst[:] for lst in A]
        for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            ni, nj = ci+di, cj+dj

            # 범위 체크
            if not (1 <= ni <= N and 1 <= nj <= N):
                continue
            if A[ni][nj] > 0 :
                cnt += 1

        A[ci][cj] += cnt
        # print(ci, cj, cnt)


    # step 5. 새로운 구름 생성
    for i in range(1, N+1):
        for j in range(1, N+1) :
            if A[i][j] >= 2 and (i, j) not in v:
                A[i][j] -= 2
                q.append((i, j))

    # test
    # for a in A[1:]:
    #     print(*a[1:])
    # print()

# [3] 시뮬레이션 정답
ans = 0
for i in range(1, N+1):
    for j in range(N+1):
        ans += A[i][j]
print(ans)

