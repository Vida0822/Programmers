class Solution {
    public int solution(String s) {
        // n = 1000 --> O(N^2) 도 ㄱㅊ (완전탐색 수행)
        // 시뮬레이션 문제--> 문제에서 제시한 과정을 코드로 옮김 
        
        int answer = s.length() ; 
        
        // 1개 단위(step)부터 압축 단위를 늘려가며 확인 (절반 나누기까지)
        for(int step = 1 ; step < s.length() / 2 + 1 ; step++){
            String compressed = "" ; 
            String prev = s.substring(0, step) ; // 앞에서부터 step만큼의 문자열 추출 
            int cnt = 1 ; 
            
            
            for(int j = step; j < s.length() ; j+= step){
                // 단위 크기만큼 뒤의 문자열 잘라서 
                String sub ="" ; 
                for(int k = j ; k < j+step ; k++){
                    if(k < s.length())
                        sub+=s.charAt(k) ; 
                }
                // 이전 문자열과 같은지 확인 
                if(prev.equals(sub))  // 같으면
                    cnt++ ;  // 개수 증가 
                else{ // 다르면 
                    // 압축 진행 
                    compressed += (cnt >= 2)? cnt+prev: prev ; 
                    // 초기화 
                    sub = "" ; 
                    for(int k = j ; k < j+step ;k++){
                        if(k < s.length())
                            sub+= s.charAt(k) ; 
                    }
                    prev = sub ; 
                    cnt=1 ; 
                }
            }
            // 남아있는 문자열 처리 
            compressed += (cnt >= 2)? cnt+prev : prev; 
            answer = Math.min(answer, compressed.length()) ; 
        }
        return answer ; 
    }
}