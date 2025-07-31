def solve() :
    N = 19
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 전체 좌표 순회하면서
    for j in range(19):
        for i in range(19):
            st = arr[i][j]

            # 2. 해당 좌표 돌이 검or흰이면
            if st == 1 or st == 2:
                ans = (i+1, j+1)

                # 3. 상/하/좌/우/대각선
                for di, dj in ((1, 0), (0, 1), (1, 1), (-1, 1)):
                    
                    # 반대 방향에 같은 돌이 있으면 cnt 개수 안맞으므로 continue 
                    back_i, back_j = i-di, j-dj
                    if (0 <= back_i < N) and 0 <= back_j < N and arr[back_i][back_j] == st :
                        continue
                    ni, nj = i, j
                    cnt = 1
                    while True:
                        ni += di
                        nj += dj
                        if not (0 <= ni < N and 0 <= nj < N):
                            break
                        if arr[ni][nj] == st:
                            cnt += 1
                           # ans.append((ni+1, nj+1))
                        else:
                            break

                    if cnt == 5:
                        # print(ans)
                        return (st, ans)
    else:
        return (0, 0)

ans = solve()
print(ans[0])

if ans[0] != 0 :
    print(ans[1][0], ans[1][1])
