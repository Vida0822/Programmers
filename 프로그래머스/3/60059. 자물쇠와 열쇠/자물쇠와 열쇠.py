def rotate(key, M) : 
    # '90도 회전' 구현 
    #  0 0 0 1       0 1 0 
    #  1 0 0 0 -->   1 0 0 
    #  0 1 1 0       1 0 0
    #                0 0 1 
    # '행을 열로 바꾼다'
    # 첫번째 행 -> 끝 열 
    # 두번째 행 -> 끝에서 두번째 열 
    # 세번째 행 -> 끝에서 세번째 열 
    
    rt_key = [[0]*M for _ in range(M)]
    for i in range(M) : 
        for j in range(M): 
            rt_key[j][M-i-1] = key[i][j] # **** 잘 기억 : 실제 좌표 변화를 수식으로(숫자로) 적고 그 규칙을 좌표 자체의 '점화식'으로 표현하는게 가장 best (행,렬 개념으로 넣으면 헷갈림)
    return rt_key

def check(metrix, N):   
    for i in range(N, 2*N):
        for j in range(N, 2*N): 
            if metrix[i][j] != 1 :
                return False    
    return True 
    
def solution(key, lock): 
    # 회전 -> 이동(1:1 -> N:N) -> 이동할 때마다 완전 탐색 (key, 자물쇠 격자 숫자 합 1이상? )
    # 회전 -> 이동 -> 완전 탐색 
    # 회전 -> 이동 -> 완전 탐색 
    N = len(lock)
    M = len(key)
    # lock 배치
    metrix = [[0]*3*N for _ in range(3*N)]
    for j in range(N): 
        for k in range(N):
            metrix[N+j][N+k] = lock[j][k] 
                
    for i in range(4): 
        # ※ 어쨌든 검사 자체는 4가지 경우를 고려해야함(4번 해야함) !! 
        # ㄴ 회전 타이밍은 시점에 따라 3번일수도, 4번일수도 있지만! ex) 회전 먼저 --> 회전 4번 / 회전 마지막에 --> 회전 3번 
        # 회전 
#        rt_key = rotate(key, M) 
#       ※기존에 회전했던 key를 다시 회전해야함 (초기 key회전 X) --> key를 단순히 복사만 하는게 아닌 갱신해줘야함
       
        # move ([0,0]->[2N][2N])
        for x in range(2*N+1):
            for y in range(2*N+1): 
                # key 배치 
                for k in range(M):
                    for p in range(M): 
                        metrix[x+k][y+p] += key[k][p]
                
                if check(metrix, N):
                    return True
                
                for k in range(M):
                    for p in range(M): 
                        metrix[x+k][y+p] -= key[k][p]  
        
        key = rotate(key, M)
    return False 