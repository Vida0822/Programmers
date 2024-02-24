import java.util.*; 
class Solution {
    public int[] solution(int n, String[] words) {
        HashSet<String> set = new HashSet<>() ; // 중복 검사용 Set
    
        set.add(words[0]) ; 
        String prevWord = words[0] ; 
        for(int i = 1 ; i < words.length ; i++){
            
            // 단어를 하나씩 검사하면서 탈락자를 찾음
            String word = words[i] ; 
            
            // 탈락 경우 1: 말했던 단어를 말함 
           
            // 탈락 경우 2 : 단어를 잘못 말함  
            if(!set.add(word) 
               || !prevWord.endsWith(word.substring(0, 1))) 
                return new int[]{(i%n)+1, i/n+1}; 
            prevWord = word ; 
        } // for 
        return new int[]{0, 0} ; // 탈락자를 못찾으면 {0,0} 반환 
    } // solution 
} // class 