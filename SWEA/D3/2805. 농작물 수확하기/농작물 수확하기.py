"""
구상 시간 : 10분
구현 시간 : 10분
디버깅 포인트 : 가운데 행이 두번 더해지는 문제 --> 가운데 행은 미리 받아놓고 시작 
"""
T = int(input())

for t in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    ans = sum(arr[N//2][0:N])
    for i in range(N//2) :
        ans += sum(arr[i][N//2-i:N//2+i+1])
        ans += sum(arr[N-i-1][N//2-i:N//2+i+1])

    print(f'#{t} {ans}')
