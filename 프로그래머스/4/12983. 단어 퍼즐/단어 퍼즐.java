import java.util.* ; 

class Solution {    
    public int solution(String[] strs, String t) {
        int[] dp = new int[t.length()+1] ; 
        Arrays.fill(dp, 20000) ; 
        dp[0] = 0 ; 
        for(int i = 1 ; i < t.length()+1 ; i++){
            for(int j = 0 ; j < strs.length; j++){
                String word = strs[j] ; 
                
                if(i < word.length()) 
                    continue ; 
                
                if(word.equals(t.substring(i-word.length(), i))){
                   // if(i - word.length() == 0)
                     //   dp[i] = 1 ;
                    //dp[i-word.length()]>0
                        dp[i] = Math.min(dp[i] , dp[i-word.length()]+1) ; 
                    
                }
            }
        } 
        return dp[t.length()] == 20000? -1 : dp[t.length()] ; 
    }
}