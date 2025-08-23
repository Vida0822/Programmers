def stick(ci, cj, stk):
    cp_arr = [lst[:] for lst in arr]

    # 붙이기
    for di in range(R):
        for dj in range(C):
            ni, nj = ci + di, cj + dj
            if stk[di][dj] == 1:
                if cp_arr[ni][nj] == 1:
                    return []
                else:
                    cp_arr[ni][nj] = 1
    # for i in range(N):
    #     print(cp_arr[i])
    return cp_arr

def rotate(stk):
    # i행 -> M-i열
    cp_stk = []
    for j in range(C):
        lst = [stk[i][j] for i in range(R-1,-1, -1)]
        cp_stk.append(lst)

    return cp_stk


# 1. 시뮬레이션 준비
N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]

# 2. 시뮬레이션 실행
for _ in range(K):
    # 스티커 만들기
    R, C = map(int, input().split())
    stk = [list(map(int, input().split())) for _ in range(R)]

    # 스티커 붙이기
    flag = False
    for i in range(4):
        if flag : break
        for ci in range(0, N-R+1) :
            if flag: break
            for cj in range(0, M-C+1):
                cp_arr = stick(ci, cj, stk)
                if cp_arr:
                    arr = cp_arr
                    flag = True
                    break
        # 스티커 돌리기
        else:
            stk = rotate(stk)
            R, C = C, R
            # for s in stk:
            #     print(*s)
            # print()

# 3. 정답 출력
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] :
            ans += 1
print(ans)
