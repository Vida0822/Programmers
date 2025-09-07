"""
이동 칸 수가 클 때
1. 한번에 계산
2. lookup 테이블 활용 --> 그냥 이어붙여서 참조하는 방식 ** (아이디어 얻어가자)
"""

# [0]
R, C, M = map(int, input().split())

shk = []
# arr = [[-1]*C for _ in range(R)]
# 이번 경우 전체 좌표에서 관리하지 말고, (arr이 상어 수에 비해 크기 때문에)
# 그냥 상어의 객체 자체를 관리
for _ in range(M):
    r, c, s, d, z  = map(int, input().split())
    # arr[r-1][c-1] = (s, d-1, z)
    # shk.append((r-1, c-1, s, d, z)) # DEBUG!!!! 튜플 형태로 넣어주면 이동시 변경된 값 대입할 수 없음 (이거 계에에에속 실수한다)
    shk.append([r-1, c-1, s, d, z])

delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
H, W = 2*R-2, 2*C-2
htbl = [i for i in range(R)]+[i for i in range(R-2, 0, -1)]
wtbl = [j for j in range(C)]+[j for j in range(C-2, 0, -1)]

opp={1:2, 2:1, 3:4, 4:3}

# [1]
ANS = 0
# [0]:i, [1]:j, [2]:speed, [3]:dir, [4]: size
shk.sort(key=lambda x: (x[1], x[0])) # 열 오름차순, 행 오름차순
for j in range(C):
    # 1. 낚시왕 이동
    for i in range(len(shk)) :  # 상어를 한마리씩 검사하면서
        # 상어 마리수가 계속 달라지므로 반복문 호출할 때마다 len으로 계산해줘야함
        if shk[i][1] == j :  # 낚시꾼이 위치한 j열에 위치한 상어라면 (자동으로 가장 윗열)
            ANS += shk[i][4] # 잡기 (size 누적)
            shk.pop(i) # 상어 목록에서 지거
            break

    # 2. 상어 이동
    for k in range(len(shk)):
        if shk[k][3] >= 3:  # 우, 좌 방향
            dr = 1 if shk[k][3] == 3 else -1  # 우측 방향이면 dj가 +1, 좌측 방향이면 dj가 -1
            shk[k][1] = (shk[k][1]+shk[k][2]*dr)%W # 좌표 계산: lookup tabla index 구하고(key) -> 실제 nj 구하기 (value)  
            if C <= shk[k][1] :
                shk[k][1] = wtbl[shk[k][1]]  # 좌표 변환
                shk[k][3] = opp[shk[k][3]]  # 방향 반대

        else:  # 하, 상 방향
            dr = 1 if shk[k][3] == 2 else -1
            shk[k][0] = (shk[k][0]+shk[k][2]*dr)%H
            if R <= shk[k][0]:
                shk[k][0] = htbl[shk[k][0]]  # 좌표 변환
                shk[k][3] = opp[shk[k][3]]  # 방향 반대

    # 3. 상어 잡아먹기
    #   : 상어 정렬 후 위에서부터 작은 상어가 같은 좌표면 삭제
    shk.sort(key = lambda x: (x[1], x[0], -x[4])) # 열, 행 오름차순, 크기 내림차순
    for i in range(len(shk)-1, 0, -1) :  # 가장 끝에서 1번까지
        # 위의 상어가 나와 좌표가 같다면 나를 삭제 (크기 내림차순)
        if (shk[i][:2]) == (shk[i-1][:2]) : # 슬라이싱으로 꺼내기 때문에 튜플로 묶어서 비교
            shk.pop(i) # 그럼 나를 빼기 (내 위가 더 큰 놈이니까)

# [2]
print(ANS)