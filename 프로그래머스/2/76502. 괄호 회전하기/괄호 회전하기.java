import java.util.* ;
class Solution {
    public int solution(String s) {
        
        int answer = 0 ; 
        for(int i = 0 ; i < s.length() ; i++){
            s = rotationBracket(s) ; 
            if(isProper(s))
                answer++ ; 
        }
        return answer ;
    }
    
    static String rotationBracket(String s){
        return s.substring(1) + s.charAt(0) ; 
    }
    
    static boolean isProper(String s){
        Stack<Character> stack = new Stack<>() ;
        
        for(int i = 0 ; i < s.length();i++){
            char c = s.charAt(i) ; 
            if(c == '[' || c == '{' || c == '(')
                stack.push(c) ; 
            else{
                if(stack.isEmpty())
                    return false ; 
                switch(c){
                    case ']' : 
                        isProperBracket(stack, '['); 
                        break ; 
                    case '}' : 
                        isProperBracket(stack,'{') ; 
                        break ; 
                    case ')' : 
                        isProperBracket(stack,'(') ; 
                        break ; 
                }
            }
        }
        return stack.isEmpty() ; 
    }
        
    static void isProperBracket(Stack<Character> stack, char bracket){
        if(stack.peek() == bracket)
            stack.pop() ; 
    }
}