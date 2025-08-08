def cal(mid, lst) :
    sm = 0 # 총 소요 예산
    for l in lst:
        if mid < l :  # 상한액보다 요청 범위가 크면 
            sm += mid # 상한액 배정
        else: 
            sm += l # 그렇지 않으면 요청 금액 배정
    return sm

def solve():
    N = int(input())
    lst = list(map(int, input().split()))
    M = int(input())

    # [0] 배열 정렬
    lst.sort()

    # 1. 전체 배정 가능한지 확인
    if M >= cal(M, lst):
        return lst[-1] # 가능한 예산액 중 최대값

    # 2. 안되면 이진 탐색

    # [1] 시작 범위 설정
    s, e = 0, lst[-1]
    ans = 0
    while s <= e:
        # [2] 중간값 구하기
        m = (s+e)//2
        if M >= cal(m, lst): # M == sm 이 아니라도 정답이 될 수 있다
            ans = m
            s = m+1
        else:
            e = m-1
    # print(m)  # 시작값을 증가시킨 후 m값을 구했을 때 불가능할 경우 s > e가되어 반복이 종료되버림
    #  --> 근데 m 값은 불가능한 값으로 저장되어있기에 가능했을 때의 이전 값을 저장해두어야함
 #   print(ans)
    return lst[-1] if lst[-1] <= ans else ans


print(solve())