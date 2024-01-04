import java.util.* ; 
import java.util.stream.* ; 

class Solution {
    public String solution(String s) {
             
        String[] str = 
            Arrays.stream(s.split(" "))
            .map(e -> Integer.parseInt(e)).sorted()
            .map(e->e+"").toArray(String[]::new) ; 
        
        return str[0] + " " + str[str.length-1] ;
        
        /*
        String[] arrStr= s.split(" ") ; 
        int[] arrInt = new int[arrStr.length] ; 

        int i = 0 ; 
        for(String part : arrStr){
            arrInt[i] = Integer.parseInt(part) ; 
            i++ ; 
        }
        
        StringBuffer sb = new StringBuffer() ; 
        sb.append(Arrays.stream(arrInt).min().getAsInt()) ; 
        sb.append(" ") ;
        sb.append(Arrays.stream(arrInt).max().getAsInt()) ; 
        return sb.toString() ; 
        */
    }
}