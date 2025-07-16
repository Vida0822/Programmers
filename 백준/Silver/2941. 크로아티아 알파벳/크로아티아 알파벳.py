A = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']
S = input()

cnt = 0 
for a in A : 
    if a in S :
        cnt += S.count(a)
        S = S.replace(a, '*') # ※ replace()는 문자열 자체를 변경하지 않음, 반환하는 형태
# debug 2 : 알파벳끼리 겹치는 경우 O ex. dz=, z= 

print(len(S))
        
    
    