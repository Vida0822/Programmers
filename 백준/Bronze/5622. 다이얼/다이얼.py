S = input()

# step 1 : 각 숫자에 해당하는 알파벳 (숫자 따라 알파벳 분류) 
# 규칙 ?
num = '22233344455566677778889999'
        
# step 2 : 단어 문자별로 숫자 + 2로 시간 누적  
total = 0
for s in S : 
    total += int(num[ord(s)-65])+1
    
print(total)    