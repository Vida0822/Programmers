T = 10

for t in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    res = 0
    for start in range(0, 100) : # 시작점은 0행의 0~100열

        # 막대가 있는 곳에서만 시작
        if arr[0][start] == 0 :
            continue

        visited = [[False]*100 for _ in range(100)] # 건너온 가로 막대를 다시 건너지 않기 위해 방문 배열

        i, j = 0, start
        while i < 100:

            # 찾던 도착지인지 확인
            if arr[i][j] == 2:
                res = start
                break

            visited[i][j] = True
            # 양옆확인 : 범위 확인(index out of range) + '1'인지 확인 + 온 길이 아닌지 확인
            if 0 <= j-1 < 100 and arr[i][j-1] == 1 and not visited[i][j-1]:
                j -= 1
            elif 0 <= j+1 < 100 and arr[i][j+1] == 1 and not visited[i][j+1]:
                j += 1
            # 옆으로 갈데가 없으면 아래로 
            else:
                i += 1

    print(f'#{t} {res}')