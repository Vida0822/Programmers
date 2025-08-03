import collections

# 왼쪽 톱니바퀴 확인
def left(idx, dir):
    # 종료 조건
    if idx < 0:
        return
    if arr[idx][2] != arr[idx+1][6]:
        left(idx-1, -dir)
        arr[idx].rotate(dir) # deque : rotate() --> 음수:왼쪽 방향/양수:오른쪽 방향

# 오른쪽 톱니바퀴 확인
def right(idx, dir):
    # 종료 조건
    if idx > 3:
        return
    if arr[idx][6] != arr[idx-1][2]:
        right(idx+1, -dir)
        arr[idx].rotate(dir)

arr = [collections.deque(list(map(int, input()))) for _ in range(4)]
K = int(input())

for _ in range(K):
    i, d = map(int, input().split())
    i -= 1

    left(i-1, -d) # 왼쪽 회전
    right(i+1, -d) # 오른쪽 회전
    arr[i].rotate(d)  # 현재 회전

ans = 0
for i in range(4):
    if arr[i][0] == 1:
        ans += 2**i

print(ans)

