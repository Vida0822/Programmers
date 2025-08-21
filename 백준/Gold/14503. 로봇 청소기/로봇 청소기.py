"""
[개인 코드 리뷰]
소요 시간: 45분
타임라인 : 이해 및 구상 : 8분 - 구현 : 14분  - 디버깅 : 23분
한줄평: 디버깅을 구역을 나눠 부분부분 해나가는게 중요할 것 같다 (전체를 보며 디버깅하니 매우 어렵다) 

[구상]
(good)
- 후진,전진 함수를 호출하는 조건을 메모할 때, 단순히 문제에서 언급한대로가 아닌 '코드식'으로 써놓아 구현할 때 편했다
    ex) '청소하지 않은 빈칸' --> '방문 False & 빈칸 True'

(bad)
- 각 함수의 입출력을 적어놓지 않아 구현할 때 헷갈렸다.
- delta 내 변환 등 헷갈리면 손코딩으로 미리 시뮬레이션 했어야 한다 (어중간하게 암기한거 주의...) .
- 조건 같은 경우, 단순히 나열식으로 쓰지 말고 번호를 붙여 인덱싱한다면 헷갈리지 않고 쓸 수 있을 듯


[구현]
(good)
- 함수를 구현하기 전 input/output 값 먼저 적어놓으니 실수하지 않았다.
- 중간중간 단계를 구분하는 주석을 달아 디버깅이 용이했다.

(bad)
- 구현 속도가 여전히 느리다.
- 입력을 정확하게 받지 않는다 (입력 순서 실수함)
- 타자 속도가 느리고 오타를 많이 낸다 (특히 주석이랑 번갈아 쓰면서 한/영 변환X)
- 구현하는 순서가 오락가락한다
    => 구현할 순서를 큰 단위로 정해놓을 필요가 있을 듯 (ex. main -> 함수1 -> 함수 2)
- 구현 도중 조건 확인 위해 문제를 다시 읽는 경우 多 : 부분부분 읽다가 오히려 잘못 해석해서 실수할 가능성 有
    => 조건은 손코딩에 명료하게 정리해서 바로바로 구현

[디버깅]

1. 시간 사용/단계별 실패 원인 추측 --> 최종 성공 시 실제 실패 원인과 비교 + 개선 기록
- 예상한 실패 원인 : 청소 처리(방문 처리)가 제대로 되지 않았다고 생각
- 실제 실패원인 : 후진 구현할 때 반대 방향 델타 참조

2. 처음 이해한 문제조건 -> 바로잡은 문제조건
- 후진할 때 방문여부는 상관없으니, 청소도 다시 한것으로 처리해도 (방문처리) 상관없다.
-> 청소 cnt 는 최초 청소시 1번만 인정되기 때문에 재방문은 가능하더라도 청소 cnt 포함은 방문 여부를 따져야한다
=> 청소처리(방문처리) 코드에 조건문 추가 : '미방문시'

- '청소 X 빈칸이면 전진' : 90도 돌린 방향이 빈칸이 아니라면 다시 while문을 돈다
-> X : 빈칸이 존재한다는건 확실하기 때문에 돌린 방향에 빈칸이 없다면 빈칸이 나올때까지 회전시켜서 해당 turn 에 전진 시켜야한다.

3. 치명적 실수
delta 기법 관리 : 꼭 암기하자 --> 반대방향 index는 (cd-2)%4 ****
"""


delta = {0: (-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)} # 북, 동, 남, 서

def back(ci, cj, cd):

    di, dj = delta[(cd-2)%4]
    ni, nj = ci+di, cj+dj
    if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] == 1 :
        return -1, -1

    return ni, nj


def front(ci, cj, cd, v):

    ni, nj = ci+delta[cd][0], cj+delta[cd][1]

    if not (0 <= ni < N and 0 <= nj < M) :
        return ci, cj
    if arr[ni][nj] == 1 or v[ni][nj] == 1:
        return ci, cj

    return ni, nj


# 입력
N, M = map(int, input().split())
si, sj, sd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 청소 시작
def solve(ci, cj, cd):
    ANS = 0
    v = [[0]*M for _ in range(N)]

    while True :
        # 1. 해당 칸 청소
        if not v[ci][cj]:
            v[ci][cj] = 1
            ANS += 1

        # 2. 주변 4칸 확인
        cnt = 0
        for di, dj in delta.values():
            ni, nj = ci+di, cj+dj

            # 범위 체크
            if not (0 <= ni < N and 0 <= nj < M):
                continue

            # 청소X + 빈칸 O 인지 확인
            if v[ni][nj] == 0 and arr[ni][nj] == 0:
                cnt += 1

        # 3. 이동 : case 1/2
        if cnt == 0:
            ci, cj = back(ci, cj, cd)
            if ci == -1 and cj == -1 :
                return ANS
        else:
            ni, nj = ci, cj
            while ni == ci and nj == cj :
                cd = (cd-1)%4
                ni, nj = front(ci, cj, cd, v) # 빈칸으로 갈 때까지 회전
            ci, cj = ni, nj

    return ANS


print(solve(si, sj, sd))
