"""
강사님 코드
- 문제에서 인덱스를 지정해준 경우 그대로 맞춰서 풀이
- 가위바위보 승패: lookup 테이블 활용
"""
# a 번호가 지는 경우
# tbl = [0, 2, 3, 1]
tbl = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

def game(l, r):
    # [1] 종료조건 : 한명인 경우 더이상 진행하지 않음
    if l == r:
        return l

    # [2] 단위/재귀: 절반으로 나눠서, 각 우승자 선정하고, 그 중 승자 인덱스 리턴
    # [2-1] 절반으로 (재귀)
    m = (l+r)//2
    a = game(l, m)  # 좌측 절반의 승자
    b = game(m+1, r) # 우측

    # [2-2] a, b중 승자 리턴 (단위)
    # if (lst[a]%3) + 1 == lst[b]:  # b가 이기는 경우
    if tbl[lst[a]][lst[b]]:
        return b
    else:   # a가 이기거나 비기는 경우
        return a


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = [0]+list(map(int, input().split()))

    ans = game(1, N) # 인덱스 반환 받음
    print(f'#{tc} {ans}')
