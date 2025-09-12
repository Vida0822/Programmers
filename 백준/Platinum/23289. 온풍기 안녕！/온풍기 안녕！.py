# [0]
R, C, K = map(int, input().split())
inarr = [[0]*(C+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(R)]+[[0]*(C+2)]

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

W = int(input())
wall = [[[0]*5 for _ in range(C+2)] for _ in range(R+2)]

for _ in range(W):
    i, j, t = map(int, input().split())
    if t == 0: # 위로 갈때 & 위에서 현재 위치(아래) 올 때 벽
        wall[i][j][3] = wall[i-1][j][4] = 1 # DEBUG!!!!!!!!!!! 벽 정확히 적어줘야지...
    else:
        wall[i][j][1] = wall[i][j+1][2] = 1

mlst = [] # 온도 측정
hlst = [] # 온풍기(시작 좌표, 방향)
for i in range(1, R+1) :
    for j in range(1, C+1):
        if 1 <= inarr[i][j] <= 4: # 온풍기
            hlst.append((i, j, inarr[i][j]))
        elif inarr[i][j] == 5: # 측정 지점 -> list로 저장
            mlst.append((i, j))

dr_dct = {1:((3, 1), (1, ), (4, 1)), 2:((4, 2), (2, ), (3, 2)),
          3:((2, 3), (3, ), (1, 3)), 4: ((1, 4), (4, ), (2, 4))}

# [1]
from collections import deque
def bfs(si, sj, dr):
    '''
    특정 온풍기(si, sj)에서 바람 부는 함수
    :param si, sj:
    :param dr: 온풍기가 바라본는 방향
    :return:
    '''
    # [0]
    q = deque()
    v = [[0]*(C+2) for _ in range(R+2)]

    # [1]
    si, sj = si+di[dr], sj+dj[dr]
    q.append((si, sj, dr))
    v[si][sj] = 5  # 바람이 나오면 누적되는 값
    arr[si][sj] += 5 # -> arr에도 동시 반영 가능 (복제본 필요 X: 고정값 전달하므로)

    # [2]
    while q:
        ci, cj, dr = q.popleft()

        # 벽
        # dr_dct에 들어있는 방향들을 모두 성공해야 확산 가능
        for dirs in dr_dct[dr]: # ((3, 1), (1, ), (4, 1))
            # 중간 좌표 갱신 필요!! (중간에 한번 타고가기 때문에)
            si, sj = ci, cj
            if v[ci][cj] == 1 : # 종료 조건 추가 : 0부터는 넣어주지 않음
                continue
            for dir in dirs:
                ni, nj = si+di[dir], sj+dj[dir]

                # 범위내,                           현재 위치에서 해당 방향으로 벽 X    미방문
                if (1 <= ni <= R and 1 <= nj <= C) and wall[si][sj][dir] == 0 and v[ni][nj] == 0 :
                    si, sj = ni, nj  # 현재 위치를 시작으로 다음 방향 체크
                else:
                    break
            else:  # 모든 방향에 만족
                q.append((ni, nj, dr)) # dr 기존거 전달!! (중간 방향 전달하지 않도록 주의!!)
                v[ni][nj] = v[ci][cj]-1
                arr[ni][nj] += v[ni][nj]
                # DEBUG !!!! : 들여쓰기 한번 안함 -> 모든 3방향이 다 갈 수 있든 없든 break 문이 아예 안걸리기때문에
                # 마지막 ni, nj (조건 불충분하더라도) 가 무조건 q에 삽입됨
                # => 계속 불가능한 좌표 탐색



# 온도가 적힌 격자 : 계속 누적해서 저장됨
arr = [[0]*(C+2) for _ in range(R+2)]
for ans in range(1, 101):
    # [1] 모든 온풍기 바람 확산 => BFS (ahe
    for si, sj, dr in hlst:
        bfs(si, sj, dr)

    # [2] 온도 조절: 모든칸 기준(인접 4방향, 벽이 없는 경우 온도차이/4 만큼 증가)
    # '동시에 발생' <=> 복사본 활용
    narr = [x[:] for x in arr] # 데이터는 arr를 보고, 업데이트는 narr에 !
    for i in range(1, R+1):
        for j in range(1, C+1): # 모든 기준 좌표
            for dr in range(1, 5): # 4방향 (헉 난 이거 2방향만 했는데... 4방향 처리하면 중복 처리하는 문제는 어떻게 해결하지? 이거 중심으로 보자)
                if wall[i][j][dr] == 0: # 벽이 없다면
                    ni, nj = i+di[dr], j+dj[dr]
                    if 1 <= ni <= R and 1 <= nj <= C:
                        val = (arr[i][j]-arr[ni][nj])//4
                        if val > 0:
                            # 0이 아니면 나눠주는 로직!!!
                            # 동일한 두 인접칸이라도 전해주는 주체가 다르기 때문에
                            # 따로 arrisited 배열 필요 없이 그냥 자기꺼 주면 주고 받는거 구현됨 !
                            narr[i][j] -= val
                            narr[ni][nj] += val

    arr = narr

    # [3] 바깥쪽 온도 1감소
    for j in range(1, C+1):
        arr[1][j] = max(0, arr[1][j]-1)
        arr[R][j] = max(0, arr[R][j]-1)
    for i in range(2, R): # ※ 여기 잘못하면 중복으로 두칸 빼준다!!!!!!!!!!! 엄청 주의!
        arr[i][1] = max(0, arr[i][1]-1)
        arr[i][C] = max(0, arr[i][C]-1)


    # [4] 조사위치 온도측정 (>= K 인경우 중단)
    for i, j in mlst:
        if arr[i][j] < K:
            break
    else:
        break  # 성공한 경우

else:
    ans = 101

# [2]
print(ans)
