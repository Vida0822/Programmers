import sys
sys.setrecursionlimit(500000)

def dfs(ci, cj) :
    v[ci][cj] = 1

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
        ni, nj = ci+di, cj+dj

        if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 255 and v[ni][nj] == 0 :
            dfs(ni, nj)


# 1. 그래프 만들기 (픽셀 입력하기)
N , M = map(int, input().split())
graph = [[0]*M for _ in range(N)]

# 픽셀을 계산하고 바로 T로 비교하기 위해 입력을 따로 받아줌 : input_arr
input_arr = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

for i in range(N) :
    lst = input_arr[i] 
    
    for j in range(0, M*3-2, 3) :
        if T <= sum(lst[j:j+3])/3 :  # T < 3개의 픽셀값을 더해 평균한 값 
            graph[i][j//3] = 255 # 255 로 변경 
#        else :    
#             pass   --> 초기값이 이미 0으로 설정되어있다. 

# 2. 전체 좌표 완전 탐색
res = 0 # 그룹 cnt : 이어져있지 않는 255들의 묶음 
v = [[0]*M for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        
        # 좌표값이 255면, 해당 그룹에 속하는 좌표 찾기 위해 dfs() 실행 
        if graph[i][j] == 255 and v[i][j] == 0 :
            res += 1 # 그룹 count 수 += 1 
            dfs(i, j)

print(res)