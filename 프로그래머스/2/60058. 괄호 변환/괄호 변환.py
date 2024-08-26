# 구현 + dfs 문제 
# 재귀함수 : u를 분리하는것 (균형잡힌 괄호 추출)

def check(u) : 
    u = list(u)
    stack = []
    for c in u : 
        if c == '(':
            stack.append(c) 
        else: 
            if len(stack) == 0 :
                return False 
            stack.pop()
    return True  

def correct(u) :   
    result = ""
    for i in range(1,len(u)-1):
        if u[i] == "(":
            result += ")"
        else : 
            result += "("
    return result 

def dfs(p):
    # 종료 조건 
    if len(p) == 0 : 
        return ""
    
    # 문자열 나누기 
    u = ""
    v = ""
    sum = 0
    for i in range(len(p)) : 
        if p[i] == "(" : 
            sum += 1 
        else : 
            sum -= 1         
        
        u += p[i]
        if sum == 0 : 
            v += p[i+1:len(p)]
            break
 #   print("u:"+u)
 #   print("v:"+v)
    if check(u) :
        return u+dfs(v) 
    else : 
 #       print("corrected u :" + correct(u))
        return "("+dfs(v)+")"+correct(u)

def solution(p) : 
    if check(p) : 
        return p
    return dfs(p) 