"""
[조건] --> 이렇게 조심해야할 값 범위 적어놓고 하는거 좋은 듯!
- -10억 <= 최소
- 최대 <= 10억

[접근]
순열 : v 배열 필요
=> N-1개의 연산자를 나열 & 계산식에 반영

* 방문 배열 : 대신 연산자 개수를 -,+ 반복하며 백트래킹
(사용할 수 있는 + 연산자가 남아있으면 사용한 순열 구하고, 다 구하면 마이너스...)

"""
def cal(ans):
    s = A[0]
    for i in range(1, N):
        c = ans[i-1]

        if c == 0:
            s += A[i]
        elif c == 1:
            s -= A[i]
        elif c == 2 :
            s *= A[i]
        else:
            if s < 0:
                s = -(abs(s)//A[i])
            else:
                s //= A[i]
    return s


def dfs(n, ans):
    global ANS_MAX, ANS_MIN

    # [0] 종료 조건
    if n == N:
        ret = cal(ans)
        ANS_MAX = max(ANS_MAX, ret)
        ANS_MIN = min(ANS_MIN, ret)

        return

    # [1] 재귀 호출
    for j in range(4):
        if OP[j] != 0:
            OP[j] -= 1
            ans.append(j)
            dfs(n+1, ans)
            OP[j] += 1
            ans.pop()


N = int(input())
A = list(map(int, input().split()))
OP = list(map(int, input().split()))


ANS_MAX = -10**9
ANS_MIN = 10**9

v = [0]*N # 순열 -> 방문 배열 필요
dfs(1, [])

print(ANS_MAX)
print(ANS_MIN)