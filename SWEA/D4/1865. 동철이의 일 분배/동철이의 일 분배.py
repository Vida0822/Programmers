"""
- 순열 : i(이전 선택) 필요 X -> v(방문 배열)만 필요
- 조합 : v (방문 배열) 필요 X -> i (이전 선택) 만 필요

※ 순서가 있는 조합은 순열이다 ex) 서로 다른 직원 3명 -> 일거리 3개
==> 일거리 3개를 뽑아서, 나열

N == 16 --> 가지치기 무조건 필요 (16^16)
"""

def dfs(n, mul): # 레벨, 누적곱, 방문 배열
    global ANS

    # 가지치기** : 확률이 무조건 1 이하이므로 곱할수록 작아짐, 이미 ANS값 보다 작다면 가망 X
    if mul <= ANS :
        return

    # [0] 종료 조건
    if n == N:
        # ANS = max(ANS, mul)
         # ANS < mul :  
        if ANS <= mul : 
            # debug(극단적 edgecase): 모든 작업 확률이 100%이라면, 16명을 특정 조합으로 작업했을 때 100%, 
            # 그리고 그 이후 어떤 작업자가 와도 100%를 넘지 않는데 작을 때만 검사를 종료하면 결국 모든 직원 조합에 대해 검사하게 됨 --> 16^16 
            # => 작거나 같을때를 가지치기 조건으로! 
            ANS = mul 
        return

    # [1] 재귀 호출
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, mul*per[n][j])
            v[j] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    per = [list(map(lambda x: x/100, map(int, input().split()))) for _ in range(N)]
    # 암기!! 입력받은 값을 map(lambda~, ) 를 통해 한번에 변환하는 방법 ! (정수 퍼센트 --> 소수 로 변환)

    ANS = -1
    v = [0]*N
    dfs(0, 1)
#    print(f'#{t}', "{:f}".format(round(ANS*100, 7)))
    print(f'#{t} {ANS*100:.6f}') # 암기 : 소수점 포맷팅 출력 -> [값:.출력할자리수f]
