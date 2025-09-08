"""
조건
- 행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다.
- 종료 조건: 행이나 열이 타일로 가득 찬 경우
 -> 정답 처리 : 연한 칸 블록있는 경우

--System--
Input : 볼록 놓은 횟수(N) -> 놓는 볼록 타입(t), 위치(i, j) --> xN
Output
1. 최종 점수
2. 파란색, 초록색 보드에 타일이 들어가있는 '칸'의 개수
"""

# [0]
N = int(input())
games = [list(map(int, input().split())) for _ in range(N)]
green = [[0]*4 for _ in range(6)]
blue  = [[0]*4 for _ in range(6)]
debug = 0

# [1]
from collections import deque

def find_max(arr, js):
    mn_j = 7
    for j in js:
        for i in range(5, -1, -1):
            if arr[i][j] == 1:
                mn_j = min(mn_j, i-1)
    return mn_j # 현재 해당 열에있는 블럭 중 가장 위에 있는 블럭 위치


def move(blocks, color): # *** 핵심
    global ANS
    global green, blue
    '''
    블럭을 이동시키는 함수
    - 이 때, 해당 행이 가득 찼다면 
        1. 해당 행을 삭제하고
        2. 점수 획득
        3. 중력 작용 -> 빈 리스트랑 합쳐주기 
    :param blocks: 이동시킬 블럭들의 빨간 보드위 블럭 좌표
    :param color: 이동 대상 보드
    :return: X -> global arr에 표시,
    '''
    # 1. 보드 특정하기
    if color == 'G' :
        arr = green # 얕은 복사 맞겠지..?
    elif color == 'B':
        arr = blue

    # 2. 놓을 수 있는 행 mx 찾기
    js = set(j for _, j in blocks)
    cnt_mx = find_max(arr, js)
    # print(cnt_mx)

    # 3. 다른 블록 만날 때까지 블럭 옮기기
    while blocks:
        ci, cj = blocks.popleft()
        for i in range(cnt_mx+1):
            ni, nj = ci+i, cj

            # 범위 밖
            if ni == 6 : # ni == 6
                arr[ni-1][nj] = 1
                break
            # 다른 블럭이 없다면
            if arr[ni][nj] == 0:
                continue

            # 다른 블럭이 있다면
            else:
                arr[ni-1][cj] = 1  # 그 전 위치로 블럭 놓기
                break
        else:
            arr[ni][nj] = 1

        for i in range(6):
            if arr[i].count(1) == 4:
                arr.pop(i)
                arr.insert(0, [0] * 4)  # 새로운 행 삽입 (중력 작용)
                ANS += 1  # 정답 처리

def check(color):
    '''
    연한 칸의 블록 존재 여부를 체크 하는 함수
    :param color: 보드 특정
    :return: X -> 있는만큼 보드 상태 변경 : 빈리스트+green[:-1]
    '''
    # 1. 보드 특정하기
    if color == 'G' :
        arr = green # 얕은 복사 맞겠지..?
    elif color == 'B':
        arr = blue

    # 2. 행/열 삭제
    for i in range(2):
        if arr[i].count(1) > 0 :
            arr.pop()
            arr.insert(0, [0] * 4)


ANS = 0
t = 1
for play in range(N) : # O(10^4)
    # print("############# PLAY: ", t, "##############")
    t += 1

    # 1. 볼록을 놓는다.
    t, i, j = games[play]
    g_blocks = deque() # 존재하는 블럭
    b_blocks = deque() # 존재하는 블럭
    if t == 2 :
        g_blocks.append((0, j+1))
        b_blocks.append((1, i))
    elif t == 3:
        g_blocks.append((1, j)) # 행열 바꿔서 넣어줘야함
        b_blocks.append((0, i+1)) # 행열 바꿔서 넣어줘야함
    g_blocks.append((0, j))
    b_blocks.append((0, i))
    debug = 1

    # 2. 블럭 이동 : 옮기기, 점수 갱신, 맵 변경
    move(g_blocks, 'G')
    debug = 2
    move(b_blocks, 'B')
    debug = 2

    # 3. 조건 검사: 연한 블럭
    check('G')
    debug = 3
    check('B')
    debug = 3

# [2]
debug = 4
print(ANS)
gr = bl = 0
for i in range(2, 6):
    for j in range(4):
        if green[i][j] == 1 :
            gr += 1
        if blue[i][j] == 1 :
            bl += 1
print(gr+bl)
