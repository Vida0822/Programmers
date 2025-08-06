T = int(input())
 
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 #   arr_rev = list(map(list, zip(arr)))
  #  arr_rev = list(map(list, zip(*arr))) # 열로 묶어서 -> 리스트로 바꾸고 -> 그걸 요소로 2차원 리스트
 
 
    res = 0
    # i행과 i열을 검사할 것
    for i in range(N):
 
        # 가로
        sm = 0 # 입력 가능한 칸 개수 (연속)
        for j in range(N) :
            if arr[i][j] == 1 : # 입력 가능하면
                sm += 1 # 칸 수에 누적
            else :
                res += max(0, sm == K)  # 입력 가능한 누적칸의 개수가 K와 같으면 result에 +1
                sm = 0
        else :
            res += max(0, sm == K) # 마지막 요소가 1 일 경우 대비
 
        # 세로 (가로와 로직 동일)
        sm = 0
        for j in range(N):
            if arr[j][i] == 1:
                sm += 1
            else :
                res += max(0, sm == K)
                sm = 0
        else :
            res += max(0, sm == K)
 
    print(f'#{t} {res}')