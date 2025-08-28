TC = int(input())

for _ in range(TC):

    # [0] 시뮬 준비
    N = int(input())
    A = [list(input()) for _ in range(N)]
    # 로봇 : 1 ~ N에 위치
    M = len(A[0])
    A = [[0]*M] + A

    # [1] 시뮬 실행
    loser = set()
    # 1. 각 경기 진행
    for k in range(M):
        # 2. 패 수집
        game = set()
        for i in range(1, N+1): # 로봇 : 1 ~ N에 위치
            if i not in loser :
                choice = A[i][k]
                game.add(A[i][k])

        # 3. 승패무 결정
        if len(game) in (1, 3) :
            continue
        else:
            if 'R' in game and 'P' in game:
                lose_choice = 'R'
            elif 'R' in game and 'S' in game:
                lose_choice = 'S'
            elif 'S' in game and 'P' in game:
                lose_choice = 'P'

        # 4. loser는 경기에서 out
        for i in range(1, N+1):
            if A[i][k] == lose_choice:
                loser.add(i)

    # [2] 시뮬레이션 정답
    ans = []
    for i in range(1, N+1):
        if i not in loser:
            ans.append(i)

    if len(ans) == 1:
        print(ans[0])
    else:
        print(0)