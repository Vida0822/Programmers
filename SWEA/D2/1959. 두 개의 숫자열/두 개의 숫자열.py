# [Sliding Window 사용]
T = int(input())
for t in range(1, T+1) :
 
    # input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    # 이후 로직 동일하게 적용하기 위해 길이 경우에 따라 big, small로 재할당
    if N > M :
        big = A
        small = B
    else:
        big = B
        small = A
 
    # 범위합 최소값 : -20*100
    res = -2000
    for i in range(len(big)-len(small)+1): # sliding window 시작 위치
        sel = list(zip(small, big[i:i+len(small)])) # 작은쪽 길이만큼 범위를 잡고 열묶음
        res = max(res , sum(s*b for s, b in sel))  # 각 열 곱한값 더하고 결과값 갱신
 
    # output
    print(f'#{t} {res}') # 여기서 계속 'T'로 적는 실수 多 (다음엔 하지 말기)
