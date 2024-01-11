import java.util.* ; 
class Solution {
    boolean solution(String s) {
        
        Stack stack = new Stack() ; 
        for(int i = 0 ; i < s.length() ; i++){
            char c = s.charAt(i) ; 
            if(c == '('){
                stack.push(c) ; 
            }else{
                if(stack.size() == 0)  
                    // stack size가 0인데 ')'가 나온 경우
                    return false ; 
                stack.pop() ; 
            }
        }
        return stack.size()==0?true:false ;
    }
}