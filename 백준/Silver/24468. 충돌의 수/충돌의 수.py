"""
조건
- idx 0과 N은 벽 --> 공이 위치할 수 있는 inx : 1 ~ N-1
"""

def move(ci, cd):
    global CNT

    # 정상 진행 시 좌표
    ni = ci + cd
    nd = cd

    # 벽인지 확인
    if ni <= 0 or ni >= L:
        nd = 0-cd

    # 공인지 확인 : 조건1) 공이 있음, 조건2) 방향이 반대임
    if len(lst[ni]) >= 1 and cd != lst[ni][0]:
        # 굳이 방향을 바꿔줄 필요 없다! 그냥 그 두 공이 교차해서 지나가도 동일
        # (따로 공 일련 번호가 있는게 아니기 때문에)
        CNT += 1
        lst[ni][0] = 0-lst[ni][0]
        nd = 0-cd


    lst[ci].pop(0)
    lst[ni].append(nd)

    return ni


# [0] 필요한 자료형
L, N, T = map(int, input().split())
lst = [[] for _ in range(L+1)] # 공 위치 : 1 ~ 7, 벽 : 0, 8
q = []

for i in range(1, N+1):
    S, C  = input().split()

    S = int(S)
    C = 1 if C == 'R' else -1

    q.append(S)
    lst[int(S)].append(C)


# [1] 시간 1초 지날때마다
CNT = 0
for _ in range(1, T+1):
    # [2] 각각의 공을 조회해서
    nq = []
    while q :
        # [3] 이동 & 다시 조회할 공으로 삽입
        c = q.pop()
        nq.append(move(c, lst[c][0]))  # 일련번호, 인덱스, 방향
    q = nq


# [4] 충돌 횟수 반환
print(CNT)