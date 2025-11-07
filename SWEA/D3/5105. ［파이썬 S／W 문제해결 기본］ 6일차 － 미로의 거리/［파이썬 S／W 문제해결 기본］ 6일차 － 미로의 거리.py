"""
풀이 시간 60분
- 구상 : 10분, 구현: 10분, 디버깅: 40분 (ㅠㅠ)

[디버깅 포인트]
v 배열과 adj 배열을 헷갈려 사용
--> 완전히 익힐 때까지 각각의 배열 역할 및 요소의 의미 적어두고 하면 좋을듯
+ 실수 ex) 범위 체크 누락 
"""

def bfs(i, j) :
    # 초기화 (시작지점)
    v = [[0] * N for _ in range(N)]
    v[i][j] = 1
    q = [(i, j)]

    while q :
        i, j = q.pop(0)

        for di, dj in ((-1, 0) , (1, 0), (0, -1), (0, 1)) :

            ni, nj = i+di, j+dj
            if not (0 <= ni < N and 0 <= nj < N) :
                continue

            if adj[ni][nj] != 1: # 벽이 아니면
                if adj[ni][nj] == 3: # 목적지이면
                    return v[i][j] # 지금까지의 이동 칸 수 반환
                elif adj[ni][nj] == 0 : # 갈수 있는 통로면(=2가 아니면)
                    if v[ni][nj] == 0:
                        v[ni][nj] = v[i][j] + 1 # 지나간 칸 수를 더해야하므로 +1 
                        q.append((ni, nj))
    return 1


T = int(input())
for tc in range(1, T+1) :

    # 1. 그래프 만들기
    N = int(input())
    adj = [list(map(int, input())) for _ in range(N)]

    # 2. 출발점 탐색
    for i in range(N) :
        for j in range(N) :
            if adj[i][j] == 2: # 출발점 발견시
                print(f'#{tc} {bfs(i, j)-1}') # bfs 호출