class Solution{
    public int solution(String s){
        // 외부 반복문 : 각 경계점에 대해 
        // 내부 반복문 : two pointer - 문자열에 한글자씩 누적하면서 양쪽이 같아지는 경우 해당 길이 반환 
        // 이 문제 특이사항 : Palindrome가 홀수인 경우, 짝수인 경우를 고려해야한다. 
        
        int answer = 0 ; 
        for(int i = 0 ; i < s.length() ; i++){
            answer = Math.max(answer, getPalindrome(s , i-1, i+1)) ; // 홀수인 경우 
            answer = Math.max(answer, getPalindrome(s , i, i+1)) ; // 짝수인 경우 
        }
        return answer ; 
    }
    
    public int getPalindrome(String s, int left, int right){
        while (left >= 0 && right < s.length() ) {
            if(s.charAt(left) == s.charAt(right)){        
                left--;
                right++;
            }else{
                break; 
            }
        }
        return right - left - 1;
    }
}