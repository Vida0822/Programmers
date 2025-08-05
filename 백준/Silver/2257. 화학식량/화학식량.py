"""
1차 시도 ) 실패..
2차 시도 ) 풀이시간 : 40분 (구상 10분, 구현 10분, 디버그 20분)

[접근]
stack(괄호 안 문자 추출)과 재귀(괄호 안 점수 계산)을 활용해 점수 계산

[디버깅]
for 문에 대한 이해 부족
: for문의 반복 변수(i)는 range 객체에서 새롭게 받아오기에 값을 본문에서 변경해도 의미 X
=> while문과 지역변수 i를 활용해 괄호 안 검사 후 그 뒤에서 검사할 수 있도록 인덱스 조정

[배운점]
1. 재귀가 메인인 로직이기에 print() 디버깅이 너무 힘들어 파이참 디버깅 기능을 활용했는데
값이 실시간으로 어떻게 변하는지 볼 수 있어서 편했다.
2. 구현 문제는 코드가 길기에 구상이 틀리면 재구상&재구현까지 너무 오랜 시간 소요
 => 최대한 완벽하고 촘촘한 설계 필요 (최소 구상 시간 10분은 무조건 구상에 집중)

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
            while True:
                i += 1
                if S[i] == '(' :
                    stack.append('(')
                elif stack and S[i] == ')' :
                    stack.pop()
                # elif S[i] not in ('(', ')'):
                if not stack :   # debug : 가장 끝에 있는 괄호 ')'는 검사 대상 문장에 포함되면 안된다
                    break
                ns += S[i]
            t = dfs(ns)
        else:
            scr += t * int(c)
            t = 0
        i += 1
    scr += t
    return scr

## main() : 
S = input()
print(dfs(S))