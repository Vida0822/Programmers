def solution(s):
    answer = len(s)
    
    # O(N^2) = O(1000^2)
    for i in range(1,len(s)//2 + 1) :  # O(N/2) : 단위를 1~N/2
        prev = s[:i]
        count = 1 
        compressed = ""
        
        for j in range(i,len(s),i): # O(N/i) : 매번 한글자~N/2글자 하나하나 확인 
            next = s[j:j+i]
            
            if prev == next : 
                count += 1 
            else :
                # 압축
                compressed += str(count) + prev if count >= 2 else prev
                
                # 초기화 
                count = 1 
                prev = next 

        # 남은 문자 압축 
        compressed += str(count) + prev if count >= 2 else prev 
        
        answer = min(answer, len(compressed))
    return answer