"""
풀이 시간 : 90분+...
-> 구상 자체를 잘못한 문제...!

[구상]
1) 좌표 완전 탐색 (BUT 열별토 탐색)
2) 각, 열에서 조사하면서 빨간색 발견시 red = True
3) 파란색을 발견했고 바로 위쪽에 빨간색을 발견했다면 --> 교착상태 ++ & red = False (이 빨간색은 그 아래로 내려가지 X)
4) 또 다른 빨간색 발견시 red = 1
5) return 교착상태 cnt

[배운점...]
처음에 수십개의 조건식으로 문제 접근...
=> 문제 설명 및 조건을 곧이곧대로 구현하기 전, 규칙성이 있는지 먼저 파악

"""
T = 10

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 여기 계속 split() 빼먹는다..

    res = 0
    for j in range(100): # 열별로 탐색
        red = False
        for i in range(100): # 행 하나씩 내리면서
            if arr[i][j] == 1 : # 빨간색 발견시
                red = True

            elif arr[i][j] == 2 and red : # 파란색 발견 & 위쪽에 내려오는 빨간색이 있으면
                res += 1 # 교착 상태 
                red = False
    print(f'#{t} {res}')

