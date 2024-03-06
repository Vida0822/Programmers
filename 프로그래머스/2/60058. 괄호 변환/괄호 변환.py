# 올바른 괄호로 변환 
def makeCorrect(u) : 
    u = list(u[1:-1]) # 첫번째와 마지막 문자 제거 + 리스트형으로 변환 
    for i in range(len(u)) : 
        if u[i] == '(' : 
            u[i] = ')'
        else : 
            u[i] = '('
    return "".join(u)   # 리스트의 각 요소를 하나의 문자열로 이어 붙여주는 함수

# 올바른 순서인지 확인 
def check_proper(u) : 
    count = 0 
    for i in u : 
        if i == '(': 
            count += 1
        else :
            if count == 0 : 
                return False
            count -= 1 
    return True   # 개수는 무조건 맞으니까(balanced_index()) 순서만 올바르면 해당 괄호는 올바른 괄호 

# 개수만 맞는지 확인 (그 개수가 맞는 index반환)
def balanced_index(p) : 
    count = 0 # 왼쪽 괄호의 개수 
    for i in range(len(p)):
        if p[i] == '(' : 
            count += 1 
        else : 
            count -= 1 
        if count == 0 : 
            return i 
        
def dfs(p):
    answer = '' 
    if p == '' :
        return answer 
    index = balanced_index(p) 
    u = p[ : index+1]
    v = p[index+1 : ]

    if check_proper(u) : 
        answer = u + dfs(v) 
    else : 
        answer = '(' + dfs(v) + ')' + makeCorrect(u) 

    return answer 

def solution(p) : 
    return dfs(p) 