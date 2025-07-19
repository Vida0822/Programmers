import copy

def color(X, Y, NM, count) : 
    if count == 1 : 
        NM[X][Y] = 'B' if NM[X][Y] == 'W' else 'W'
    for x in range(X, X+8) : 
        for y in range(Y, Y+8) : 
            if y + 1 < Y + 8 and NM[x][y] == NM[x][y+1] : 
                count += 1 
                NM[x][y+1] = 'B' if NM[x][y] == 'W' else 'W'
            if x + 1 < X + 8 and NM[x][y] == NM[x+1][y] : 
                count += 1 
                NM[x+1][y] = 'B' if NM[x][y] == 'W' else 'W'   
    return count 

N, M = map(int, input().split())
NM = []
for _ in range(N): 
    NM.append(list(input()))
    
# 완전 탐색 : 모든 위치에서 8x8을 잘라서, 
# 검은색 or 하얀색으로 시작할 때 칠해야하는 개수 --> 최소값 갱신 
ans = 100
for x in range(N-7) : 
    for y in range(M-7) : 
        ans = min(ans, color(x, y, copy.deepcopy(NM), 0), color(x, y, copy.deepcopy(NM), 1))

print(ans) 

