"""
핵심 아이디어
: 실제로 톱니 상태를 변경시키는게 아닌
회전 여부를 통해 맨 위에 오는 돌기 idx만 관리하고
그 idx 기준으로 2, 6번 등 다른 돌기를 참조
"""

# 1. 시뮬레이션 준비
T = int(input())
arr = [[0]*8]+[list(map(int, input())) for _ in range(T)]

top = [0]*(T+1)
K = int(input())

# 2. 시뮬레이션 실행 (회전)
for _ in range(K):
    tlst = []

    idx, rot = map(int, input().split())
    tlst.append((idx, 0))

    # 1) 왼쪽 톱니 검사
    for i in range(idx-1, 0, -1):
        if arr[i][(top[i]+2)%8] != arr[i+1][(top[i+1]+6)%8]:
            tlst.append((i, (idx-i)%2)) # 나랑 위치가 짝수배 차이나면 같은 방향
        else:
            break # 중간에 멈추면 그 이후 는 회전 X

    # 2) 오른쪽 톱니 검사
    for i in range(idx+1, T+1):
        if arr[i][(top[i]+6)%8] != arr[i-1][(top[i-1]+2)%8]:
            tlst.append((i, (i-idx)%2))
        else:
            break

    # 3) 회전시키기 (시계방향이면 idx에서 -1, 반시계면 idx에서 +1)
    for t, d in tlst:
        if d == 0 : # 같은 방향
            top[t] = (top[t] - rot) % 8 # 시계면 -1, 반시계면 +1 됨
        else: # 다른 방향
            top[t] = (top[t] + rot) % 8

# 3. 결과 도출하기
ans = 0
for t in range(1, T+1) :
    if arr[t][top[t]] == 1:
        ans += 1
print(ans)
# print(top)