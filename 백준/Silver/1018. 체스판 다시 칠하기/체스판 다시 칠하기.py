import copy

def color(X, Y, NM): # , count) 

    # 2. 완성된 체스판과 비교해서 count : 반복문 1번 돔 
    start_w, start_b = 0, 0 
    
    for x in range(X, X+8): 
        for y in range(Y, Y+8):
            if (x+y)%2 == 0 : 
                if NM[x][y] != 'W' : 
                    start_w += 1 
                else : 
                    start_b += 1
            else : 
                if NM[x][y] != 'W': 
                    start_b += 1 
                else : 
                    start_w += 1 
                    
    return min(start_w, start_b)                   

N, M = map(int, input().split())
NM = []
for _ in range(N): 
    NM.append(list(input()))
    
# 완전 탐색 : 모든 위치에서 8x8을 잘라서, 
# 검은색 or 하얀색으로 시작할 때 칠해야하는 개수 --> 최소값 갱신 
ans = 100
for x in range(N-7) : 
    for y in range(M-7) : 
         # ans = min(ans, color(x, y, copy.deepcopy(NM), 0), color(x, y, copy.deepcopy(NM), 1))
        ans = min(ans, color(x, y, NM))
print(ans) 

