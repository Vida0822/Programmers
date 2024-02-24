import java.util.*; 
class Solution {
    public int[] solution(int n, String[] words) {
        HashSet<String> set = new HashSet<>() ; // 중복 검사용 Set

        // 초기 상태 
        set.add(words[0]) ; 
        String prevWord = words[0] ; 
        
        // 완전 탐색 : 단어를 하나씩 검사하면서 탈락자를 찾음
        int[] answer = new int[]{0,0} ; 
        for(int i = 1 ; i < words.length ; i++){    
            
            String word = words[i] ; 
            
            // 탈락 경우 1: 말했던 단어를 말함 
            if(!set.add(word)   
               // 탈락 경우 2 : 단어를 잘못 말함  
               || !prevWord.endsWith(word.substring(0, 1))){
                answer[0] = i%n + 1;
                answer[1] = i/n + 1 ; 
                break; 
                // {탈락한 사람 번호(나머지), 자신의 몇번째에서 탈락(몫)} + 배열 index가 0부터 시작하니 +1
            }
            prevWord = word ; 
        } // for 
        return answer ; // 탈락자를 못찾으면 {0,0} 반환 
    } // solution 
} // class 