"""
풀이 시간 : 20분
- 구상 5분, 구현 5분, 디버깅 10분 ㅠㅠ

[디버깅 포인트]
- 문제를 꼼꼼히 읽지 않아 재구상에 오랜 시간 소요 ex. 0보다 작아지면 0으로 다시 넣는다, 0 이하가 될때까지 무한 반복한다 등
- 입력, 출력 형식을 정확히 보지 않아 이상한 입력값이 들어오는걸 늦게 발견
결론 : 문제를 꼼꼼히 읽자 (내용, 입력/출력, 특별조건 및 제약사항)
"""

#def solve() :
    # 1. 내 코드
    # while True: # while문 사용이 미숙하다면 무한루프로 돌리고, 빼는게 좋음
    #     for i in range(1, 6):
    #         a = q.pop(0) - i
    #         if a <= 0:
    #             q.append(0)
    #             return q
    #         q.append(a)
    # else:
    #     return q

T = 10
for _ in range(1, T+1) :
    t = int(input())
    q = list(map(int, input().split()))

    # 2. 강사님 코드
    n = 1
    while True :
        # t = q.pop(0) -n
        # if t <= 0 :
        #   t = 0
        # q.append(t)
        q.append(max(q.pop(0)-n, 0)) # pop() == popleft()

        if q[-1] == 0 :
            break

        n = n % 5 + 1  # 반복문 대신 반복되는 인덱스 세트는 나머지로 표현 가능

    print(f'#{t}', *q)
