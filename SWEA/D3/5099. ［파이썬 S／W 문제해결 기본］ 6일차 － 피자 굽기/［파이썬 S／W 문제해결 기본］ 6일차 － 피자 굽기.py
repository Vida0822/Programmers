"""
풀이시간 : 1시간 (구상 10분, 구현 10분, 디버깅 40분)

[디버깅 포인트]
문제에 주어진 조건 및 Edde case 를 고려하지 않아 생긴 문제
* N < M : 화덕 크기보다 피자 개수가 많을 때, 피자가 하나라도 빠져야 새로 넣을 수 있음
* 처음 주어진 피자가 다 구어져야 새로 넣을 수 있는게 아닌  하나라도 빠지면 넣을 수 있음
* 빠진 1번 위치에 새로운 피자 들어감 (맨 끝으로 추가되는거 X)

=> 문제 좀 제발 !! 꼼꼼히 읽고 구상/설계 꼼꼼히 하고 구현 ㅠㅠ
"""
T = int(input())
for tc in range(1, T+1) :
    N , M = map(int, input().split())
    piz = list(enumerate(map(int, input().split()), start=1))
    q = []

    # 화덕 수용 개수만큼 피자 가져오기
    if N > M :
        q = [*piz]
    else : # N < M
        q = [*piz[:N]]

    while q :
        i, c = q.pop(0)
        t = c // 2

        if c:
            q.append((i, t))
        elif N < M :
            q.insert(0, (piz[N][0], piz[N][1]))
            N += 1

    print(f'#{tc} {i}')