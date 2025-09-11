"""
핵심 아이디어
: 두개의 map 사용 ) 위치&방향 정보 map + 방문 관련 map
=> 깨달은 점:
1. 난 아직 초보니까 문제가 복잡할 때는 시간 복잡도가 너무 크지 않다면
=> 그냥 map 완탐하고 이동시키는 방식을 선호하자 (list에서 꺼내는거 이번 주말에 공부고..)
2. 꼭 모든 정보를 하나의 자료구조에 포함할 필요 없다.
=> 여러개를 사용하되, 각 로직마다 어떻게 처리할지 확실히 정해두면 good
3. 자료구조는 최대 3개 : 1. arr(대상 위치 관리) 2. v배열 (상태값 관리) 3. lookup 테이블(1~2개)
=> 그 이상 나오면 줄일 수 있는 방법 재구상
"""

# [0]
N, M, K = map(int, input().split())

# 상어 (위치, 방향) 정보
arr = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))

# 각 위치별로 특정 냄새의 상어 번호, 남은 시간을 저장하는 2차원 리스트 (***)
# => 냄새 정보를 상어 단위로 관리하지 않고 각 칸에 대해 관리하면 훨씬 편함 !
smell = [[[0, 0]]*N for _ in range(N)]
# for s in smell:
#     print(*s)
# 각 상어의 회전 방향 우선순위 정보
priorities = [[] for _ in range(M)]
for i in range(M):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# delta (상/좌/하/우)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


# [1]
def update_smell():
    '''
    모든 냄새 정보를 업데이트 하는 함수
    :return:
    '''
    # 각 위치를 하나씩 확인하며
    for i in range(N):
        for j in range(N):
            # print(i, j)
            # 냄새가 존재하는 경우 [상어idx, 냄새양]
            if smell[i][j][1] > 0 :
                smell[i][j][1] -= 1

            # 상어가 존재하는 경우 => 물고기 냄새 남기는 로직을 상어 이동할 때 하지않고 '냄새 상태를 변경시키는 함수' 안에서 상어 존재 여부에 따라 갱신
            if arr[i][j] != 0 :
                smell[i][j] = [arr[i][j], K]  # 해당 상어의 idx와 남은 유효기간을 격자에 표시

def move():
    '''
    모든 상어를 이동시키는 함수
    :return:
    '''
    # '동시에 이동' -> 무조건 new 배열
    narr = [[0]*N for _ in range(N)]

    # 각 위치를 하나씩 확인하며
    for ci in range(N):
        for cj in range(N):
            if arr[ci][cj] != 0 :
                cd = directions[arr[ci][cj]-1] # 해당 상어 idx의 방향

                # 1) 일단 냄새가 존재하지 X 곳 확인
                found = False
                for index in range(4):
                    ni = ci+di[priorities[arr[ci][cj]-1][cd-1][index]-1] # 값 자체가 1, 2, 3, 4로 들어오기 때문에 1씩 빼줘야함
                    nj = cj+dj[priorities[arr[ci][cj]-1][cd-1][index]-1]

                    if 0 <= ni < N and 0 <= nj < N :
                        if smell[ni][nj][1] == 0:  # 냄새가 존재X
                            # 상어 이동 => 관련 자료구조에 모두 update

                            # 1. 상어 방향 변경
                            directions[arr[ci][cj]-1] = priorities[arr[ci][cj]-1][cd-1][index]

                            # 2. 위치 배열 변경
                            if narr[ni][nj] == 0:
                                narr[ni][nj] = arr[ci][cj]
                            else:
                                narr[ni][nj] = min(narr[ni][nj], arr[ci][cj])
                            found = True
                            break
                if found:
                    continue

                # 2) 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    ni = ci+di[priorities[arr[ci][cj]-1][cd-1][index]-1]
                    nj = cj+dj[priorities[arr[ci][cj]-1][cd-1][index]-1]
                    if 0 <= ni < N and 0 <= nj < N :
                        if smell[ni][nj][0] == arr[ci][cj]: # 자신의 냄새가 있는 곳이면
                            directions[arr[ci][cj]-1] = priorities[arr[ci][cj]-1][cd-1][index]
                            narr[ni][nj] = arr[ci][cj]
                            break
    return narr


time = 0
while True:
    update_smell() # 모든 위치의 냄새 업데이트
    narr = move() # 모든 상어 이동 시키기
    arr = narr  # 맵 업데이트-> 이걸 arr = move()로 바로 받아버리면 이전 상태와 이후 상태가 섞여버려서 의도치 않은 동기화 오류, 버그 발생
    time += 1  # *** time 위치

    # 1번 상어만 남았는지 체크 (N이 20으로 작기 때문에 완탐)
    check = True
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 1:
                 check = False
    if check:
        print(time)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break
