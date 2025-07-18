N = int(input())  # 합친 결과가 주어짐 --> 자리수 합이 가능한지 

# 완전 탐색 : 합쳐서 N이 되는 모든 조합 
result = 0
for i in range(1, N): 
#    hap = i+sum(map(int,str(i).split())) : split() 은 공백 기준으로 나누기 때문에 분해가 X 
    hap = i + sum(map(int, str(i))) # 문자열 그대로 순회하면 자리수 하나하나 처리 ! 
    
    if hap == N :
        result = i 
        break
        
print(result)
