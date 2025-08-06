"""
[접근]
1. N개중 K개를 선택해 나열 = 순서 있는 조합 = '순열'=> v (방문 배열) 사용
2. 종료 조건 : n == K (뽑은 개수 K)
3. 이어붙여 중복인 요소는 countX --> set() 사용

"""

def dfs(n,sm, v):
    global ANS

    # [0] 종료 조건
    if n == K:
        ANS.add(sm)
        return

    # [1] 재귀 호출
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1,sm+str(lst[j]),v) # 숫자 그대로 이어붙이기 위해 문자열 변환
            v[j] = 0
            
###################################################
N = int(input())
K = int(input())
lst = [int(input()) for _ in range(N)]

ANS = set()
dfs(0, '', [0]*N)
print(len(ANS))