N, K = map(int, input().split())
A = [0]+list(map(int, input().split())) # 패딩 필요
L = 2*N

# 0. 시뮬레이션 준비 (필요한 자료형)
ans = 0
lst = [0]*(L+1)

# 1. 시뮬레이션 실행
while True:
    ans += 1  # 일자 증가

    # [0] 벨트 이동
    lst.insert(1, lst.pop())
    A.insert(1, A.pop())
    if lst[N] == 1:
        lst[N] = 0

    # [1] 로봇 이동
    cp_lst = [0]*(L+1)
    for i in range(L, -1, -1):
        if lst[i] == 1 :
            n = (i+1) % L if (i+1) % L != 0 else 2*N
            if lst[n] == 0 and A[n] >= 1: # 로봇 없음 & 내구도 있음
                lst[i] = 0
                lst[n] = 1
                A[n] -= 1
    if lst[N] == 1:
        lst[N] = 0

    # [2] 로봇 올리기
    if lst[1] == 0 and A[1] >= 1 :
        lst[1] = 1
        A[1] -= 1

    # [3] 내구도 체크
    cnt = 0
    # print(A)
    for i in range(1, L+1):
        if A[i] <= 0 :
            cnt += 1
    if cnt >= K :
        break

# 2. 시뮬레이션 정답 출력
print(ans)