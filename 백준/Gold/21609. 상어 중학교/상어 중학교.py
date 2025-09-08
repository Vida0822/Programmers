from collections import deque

def print_arr(arr):
    # for row in arr:
    #     print("".join(map(lambda x: str(x).rjust(4), row)))
    # print()
    for row in arr:
        print("".join(map(lambda x: str(x).replace('-2', '_').rjust(4), row)))
    print()


# [0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# [1]
def move():
    '''
    중력을 적용시키는 함수 : 2048(easy)의 로직 이용
    :return:
    '''

    global arr
    new_arr = []
    for j in range(N):
        t_lst = []
        blank = 0
        for i in range(N-1, -1, -1):
            n = arr[i][j]
            if n == -2:
                blank += 1
                continue
            elif n == -1:
                t_lst += [-2]*blank
                blank = 0
                t_lst.append(n)
            else:
                t_lst.append(n)
        new_arr.append(t_lst+[-2]*(N-len(t_lst)))
    arr = rotate(new_arr)

def rotate(arr):
    # global arr
    new_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[j][N-1-i]
    return new_arr

def bfs(si, sj, color):
    '''
    문제 조건에 따라 볼록 그룹에 포함시킬 블록을 포함시키는 함수

    :param si, sj: 그루핑 시작점
    :return: v(set) --> 볼록 정렬 기준이 다양하기 때문에 방문한 v 배열 자체 반환

    '볼록 그룹'
    - 일반 블록이 적어도 하나 -> bfs 호출 조건 : 일반 블럭
    - 일반 블록의 색은 모두 같아야  -> 인접...방문 조건...? !!
    - 검은색 블록은 포함되면 안 되고 -> 인접 방문 조건
    - 블록의 개수는 2보다 크거나 같아야 -> 그루핑 후 검사
    - 그룹에 속한 다른 모든 칸으로 이동 -> 이건 당연...
    '''

    global v

    # [0]
    v_local = set() # 그룹에 포함될 블럭
    q = deque()

    # [1]
    v_local.add((si, sj))
    v.add((si, sj)) # ※ 둘 다 계속 관리해줘야함..? 진심? (이거 필요 있나..? 일단 관리, 삭제 염두)
    q.append((si, sj))

    # [2]
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)) :
            ni, nj = ci+di, cj+dj

            # 범위
            if not (0 <= ni < N and 0 <= nj < N):
                continue

            # 방문 체크
            if (ni, nj) in v_local :
                continue

            # 검은 색 블록
            if arr[ni][nj] == -1:
                continue

            # 빈 블럭
            if arr[ni][nj] == -2:
                continue

            # 무지개 블럭
            if arr[ni][nj] == 0 :
                v_local.add((ni, nj))  # ※ 무지개 블럭은 여러 그룹에 포함될 수 있다!!!!!
                q.append((ni, nj))
                continue

            # 일반 블록 but 다른 그룹에 포함
            if (ni, nj) in v:
                continue

            # 일반 블록 but 다른 색
            if arr[ni][nj] != color :
                continue

            # 일반 블록 but 같은 색
            v.add((ni, nj))
            v_local.add((ni, nj))
            q.append((ni, nj))
            debug = 1

    v_local = list(v_local)
    v_local.sort(key=lambda m:(arr[m[0]][m[1]], -m[0], -m[1]))
    # 값 오름차순(0이 앞에옴, 일반 블럭 뒤에), 행,열 내림차순(작은게 뒤에옴)
    return v_local


# [오토 플레이]
# 1. 가장 큰 볼록 그룹 찾기
# 1) 그룹 만들기

ANS = 0
# t = 1
while True:
    # print("######AutoPlay : ", t, "##########")
    # t += 1
    v = set()
    groups = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and (i, j) not in v: # 일반 블럭인데 방문 X
                debug = 'BFS'
                grp = bfs(i, j, arr[i][j])

                # ~ 그루핑 후 검사 ~
                if len(grp) < 2:
                    continue
                # print(len(grp))
                groups.append(grp)

    # 종료 조건
    if not groups :
        break

    # 2) 그룹 정렬하기: 크기 /무지개 개수 /일반 블록 中 가장 큰 행,열
    # groups.sort(key=lambda grp:(len(grp), grp.count(0), grp[-1][0], grp[-1][1])) # 행열 오름차순
    # DEBUG!!!!!!!!!!!!: grp에 저장되는 애들은 그룹에 포함되는 좌표 자체기 때문에, 블럭 값 자체가 아닌데 거기서 0을 세는건 대체 뭐야...? 아니 진짜 뭐지 나...?

    groups.sort(key=lambda grp:(len(grp), list(arr[i][j] for i, j in grp).count(0), grp[-1][0], grp[-1][1])) # 행열 오름차순
    # print(groups)
    big = groups.pop()
    # print(groups)
    # print(big)
    debug = 0

    # 2. 블록 제거하기
    # print('볼록그룹 제거:', arr[big[-1][0]][big[-1][1]])
    for mi, mj in big:
        arr[mi][mj] = -2 # 제거된 블록임을 표시
    # print_arr(arr)

    # 점수 획득하기
    ANS += len(big)**2
    # print(big)
    debug = 1

    # 3. 중력 작용하기
    move()
    debug = 2
    # print('중력 1')
    # print_arr(arr)

    # 4. 회전 하기
    arr = rotate(arr)
    debug = 3
    # print('회전')
    # print_arr(arr)

    # # 5. 중력 작용하기
    move()
    debug = 4
    # print('중력2')
    # print_arr(arr)

# [2]
print(ANS)