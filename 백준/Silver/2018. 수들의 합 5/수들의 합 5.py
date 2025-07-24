# 투포인터 알고리즘
# : 슬라이딩 윈도우와 달리 조건에 따라 길이가 변화하는 특징 사용
# (start 위치를 점차 이동시키면서 조건합)

N = int(input())
start = end = 0
res = 0 # 가지수

sm = 0 # 연속하는 자연수 범위합 (가지수 구할때마다 초기화)
while end <= N:
    if sm < N: # 범위합이 N보다 작으면
        end += 1 # 숫자 하나 더 포함
        sm += end
    else: # sm == N or sm > N
        if sm == N :
            res += 1
        start += 1  # 시작 index를 옮기고 다시 한개, 두개, 세개 검사
        end = start
        sm = 0

print(res)

