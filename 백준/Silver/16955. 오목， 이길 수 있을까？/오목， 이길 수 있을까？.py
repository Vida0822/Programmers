arr = [input() for _ in range(10)]

directions = [(0, 1) , (1, 0) , (1, 1), (-1, 1)]  # 가로, 세로, 대각선(우하방향) , 대각선(우상방향)
for i in range(10) : 
    for j in range(10) : 
        if arr[i][j] == '.' : # 빈칸 일때 'X' 바둑을 놓는다고 가정
            for dx, dy in directions : # 각 방향별로 체크
                cnt = 1 
                x, y = i + dx, j + dy
                while 0 <= x < 10 and 0 <= y < 10 and arr[x][y] == 'X' :  # 가로 세로 한번에 조건 체크 
                    cnt += 1
                    x += dx
                    y += dy 
                     
                x, y = i - dx, j - dy 
                while 0 <= x < 10 and 0 <= y <= 10 and arr[x][y] == 'X' : 
                    cnt += 1 
                    x -= dx 
                    y -= dy 

                if cnt >= 5 : 
                    print(1) 
                    exit()
                

print(0)
                 