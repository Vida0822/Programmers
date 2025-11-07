T = int(input())

for t in range(1, T+1):
    N = int(input())

    tri = [[0]*N for _ in range(N)]
    tri[0][0] = 1
    for i in range(1, N) :
        for j in range(i+1) :
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]


    # 출력 분리
    print(f'#{t}')
    for i in range(N) :
        for j in range(i+1) :
            print(tri[i][j] , end = ' ')
        print()
