# 투포인터 알고리즘
# : 슬라이딩 윈도우와 달리 조건에 따라 길이가 변화하는 특징 사용
# (start 위치를 점차 이동시키면서 조건합)

N = int(input())
res = 0 # 가지수

# 1.while문
# start = end = 0
# sm = 0 # 연속하는 자연수 범위합 (가지수 구할때마다 초기화)
# while end <= N:
#    if sm < N: # 범위합이 N보다 작으면
#        end += 1 # 숫자 하나 더 포함
#        sm += end
#    else: # sm == N or sm > N
#        if sm == N :
#            res += 1
#        sm -= start
#        start += 1  # 시작 index를 옮기고 다시 한개, 두개, 세개 검사

# print(res)


# 2. for 문
# for i in range(0, N) : --> 이렇게하면 N-1 + N 까지만 가능하고 N만 포함되는게 불가능
#    sm = i
#    for j in range(i+1, N+1):
for i in range(1, N+1):  # 기준
    sm = 0
    for j in range(i, N+1): # 더할 수
        sm += j
        if sm == N:
            res += 1
            break
        elif sm > N:
            break
#        else :  --> else인 경우도 따져봐야함 (나중에 주석처리하더라도)
#            pass
print(res)
