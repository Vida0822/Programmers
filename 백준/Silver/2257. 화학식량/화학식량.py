"""
1차 시도 : 실패.. 나중에 수정
"""
score = {'H':1, 'C':12, 'O':16}

def dfs(S):
    scr = t = i = 0
    while i < len(S):
        c = S[i]
        if c in ('H', 'C', 'O') :
            scr += t
            t = score[c]
        elif c == '(':
            scr += t

            # 괄호 안에 속한 문자열 구하기
            stack = ['(']
            ns = ''
            while stack:
                i += 1
                if S[i] == '(' :
                    stack.append('(')
                elif stack and S[i] == ')' :
                    stack.pop()
                # elif S[i] not in ('(', ')'):
                if not stack :
                    break
                ns += S[i]
            t = dfs(ns)
        else:
            scr += t * int(c)
            t = 0
        i += 1
    scr += t
    return scr

S = input()
print(dfs(S))