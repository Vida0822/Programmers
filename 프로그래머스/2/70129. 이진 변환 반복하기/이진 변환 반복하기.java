import java.util.* ; 

class Solution {
    public int[] solution(String s) {
        
        int removedZero = 0 ;  
        int i = 0 ; 
        while(!s.equals("1")){
            int originLength = s.length() ; 
            s = s.replaceAll("0","");
            removedZero += (originLength - s.length()) ;   
            s = Integer.toBinaryString(s.length())+""; 
            i++;  
        }
        return new int[]{i, removedZero}; 
    }
}