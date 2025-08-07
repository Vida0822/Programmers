def dfs(n, i, scr):
    global ANS

    # [0] 종료조건
    if n == N:
        # print(v)
        if scr >= 5 :
            ANS += 1 # 정답 처리
        return

    # [1] 재귀호출
    for j in range(1, 6):
        if v[j] >= 2 : # 해당 답이 두번 연속했으면
            continue # 그 답은 pass~!
        else:
            if i == j  :
                v[j] += 1
                if A[n] == j :
                    dfs(n+1, j, scr+1)
                else :
                    dfs(n+1, j, scr)
                v[j] -= 1

            else:
                t = v[i]  # 직전 답의 연속 개수를 저장해두고
                v[i] = 0
                v[j] += 1 # 현재 답의 연속 개수를 1증가 (i == j 일 수도 있다)
                if A[n] == j :
                    dfs(n+1, j, scr+1)
                else :
                    dfs(n+1, j, scr)
                v[j] -= 1
                v[i] = t # 원상 복구

A = list(map(int, input().split()))
N = len(A)
ANS = 0

v = [0]*6
dfs(0, 0, 0)
print(ANS)
