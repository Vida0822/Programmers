T = int(input())
for t in range(1, T+1) :
    # Point : 사각형을 받아 색을 칠할 때 보라색이 된 부분을 count (끝나고 전체 탐색 X)
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
 
    res = 0
    for _ in range(N) :
        x1, y1, x2, y2, c = map(int, input().split())
 
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if arr[x][y] == 0 or arr[x][y] == c:
                    arr[x][y] = c
                elif arr[x][y] == -1:
                    pass
                else:
                    res += 1
                    arr[x][y] = -1
 
    print(f'#{t} {res}')