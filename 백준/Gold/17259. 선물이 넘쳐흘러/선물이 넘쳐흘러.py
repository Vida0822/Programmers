from collections import deque

# [0] 시뮬레이션 준비
B, N, M = map(int, input().split())

ipt = [[0]*(B-1) for _ in range(B-2)]
for _ in range(N):
    i, j, time = map(int, input().split())
    ipt[i-1][j] = time

belt = deque([0]*(3*B-2))
A = ipt[0]+[ipt[0][B-2]]+[ipt[i][B-2] for i in range(B-2)]+[ipt[B-3][B-2]]+ipt[B-3][::-1] # 각자의 작업 시간
work = [0]*(3*B-2) # 남은 작업 시간
# print(A)


# [1] 시뮬레이션 실행
ans = 0
cnt = 0
m = M
while True :

    # 작업자 시간 감소
    for i in range(3*B-2):
        if work[i]:
            work[i] -= 1

    # 1. 벨트 회전
    # p = belt.pop()
    belt.appendleft(belt.pop())

    # 2. 선물 놓기
    if m > 0 :
        m -= 1
        belt[0] = 1

    # 3. 선물 포장
    for i in range(3 * B - 3, -1, -1):
        if i == 2*B-2 or i == B-1:
            continue
        # 선물 有 & 작업자 有
        if belt[i] == 1 and A[i]:
            # 작업 가능 (배치)
            if work[i] == 0:
                ans += 1
                belt[i] = 0
                work[i] = A[i]
                if i in (B-2,  2*B-3) :
                    work[i+2] = A[i+2]
                elif i in (B, 2*B-1):
                    work[i-2] = A[i-2]
        # print(belt)


    # 4. 선물 버리기
    if belt[-1] == 1:  # 버리는 칸에 선물 있으면 버리기
        belt[-1] = 0
        cnt += 1

    # 5. 종료 조건
    if m == 0 and (ans + cnt) == M :
        break


    #
    #
    # print('m:', m, 'cnt:', cnt, 'ans:', ans)
    # print(*belt)
    # print(*work)
    # print(*A)
    # print()

# [3] 시뮬레이션 정답
print(ans)
