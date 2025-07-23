N, M = map(int, input().split())

metrix = [[0]*101 for _ in range(101)]
visible = [[True]*101 for _ in range(101)]

result = 0
for _ in range(N) :
    x1, y1 ,x2, y2= map(int, input().split())
    dx = x2-x1
    dy = y2-y1

    for i in range(x1, x2+1) :
        for j in range(y1, y2+1) :
            metrix[i][j] += 1
            if metrix[i][j] > M and visible[i][j]:
                result += 1
                visible[i][j] = False

print(result)