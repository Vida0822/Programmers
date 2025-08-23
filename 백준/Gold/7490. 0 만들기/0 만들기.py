def check(sent):
    # sent = sent.strip() --> 양끝 공백만 제거
    sent = sent.replace(' ', '')

    res = 0
    oper = ''
    flag = '+'
    for i in range(len(sent)) :
        if sent[i] in ('+', '-'):
            if flag == '+':
                res += int(oper)
            else:
                res -= int(oper)
            flag = sent[i]
            oper = ''
        else :
            oper += sent[i]

    if flag == '+':
        res += int(oper)
    else:
        res -= int(oper)
    if res == 0 :
        return True
    else:
        return False


def make_sent(ans):
    sent = ''
    for i in range(N - 1):
        sent += A[i] + ans[i]
    sent += A[N - 1]

    return sent

def dfs(n, ans):

    # [0] 종료조건
    if n == N-1:
        sent = make_sent(ans)
        if check(sent) :
            ANS.append(sent)
        return

    # [1] 재귀호출
    dfs(n+1, ans+['+'])
    dfs(n+1, ans+['-'])
    dfs(n+1, ans+[' '])

TC = int(input())
for _ in range(TC):
    ANS = []
    N = int(input())
    A = [str(i) for i in range(1, N+1)]
    dfs(0, [])

    ANS.sort()
    print(*ANS, sep='\n')
    print()