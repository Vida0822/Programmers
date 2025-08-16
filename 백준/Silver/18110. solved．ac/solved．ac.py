"""
조건
- 시간 : 1초 (복잡도 고려**), 메모리 큼 : 1024
--> O(N)

[1차 풀이] : 각 점수대별 명수를 기록하는 memoization 활용해 중간부분만 추출
--> FAIL : '동일한 점수대에 일부만 포함되는 경우' 고려한 세부 구현이 지저분해짐 (히든 TC 통과 X)
ㄴ 불가능한 세부 구현을 설계하는 경우 多
=> 설계 후 오픈 TC 시뮬레이션은 필수+코드 기준으로 설계하기(not 사람 아이디어) : 아이디어를 실제 코딩으로 구현할 때 지저분하지 않는지(조건문 덕지덕지, 변수 많아짐) 꼭 체크
(제발 급하게 구현하지 말기 오래 걸리더라도 지금은 손코딩 꼼꼼히 ㅠㅠ)

"""
from collections import deque

def solve():
    # 1. q에 입력 & 총 점수 구하기
    N = int(input())

    q = []
    sm = 0
    for _ in range(N):
        scr = int(input())
        q.append(scr)
        sm += scr


    # 2. 절사 범위 구하기
    low = int(N*0.15+0.5)
    high = N-int(N*0.15+0.5) # debug : int(N*0.85) --> 문제에서 계산 과정 제시 시 똑같이

    # 가지치기
    if high - low == 0 :
        return 0
    # 3. 정렬
    q = deque(sorted(q))

    # 4. 절사하기 : O(N*0.3)
    for _ in range(low):
        sm -= q.popleft()

    for _ in range(high,N):
        sm -= q.pop()

    # 5. 정답 출력
    return(int(sm/(high-low)+0.5))

print(solve())

