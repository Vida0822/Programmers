import java.util.* ; 
class Solution{
    public int solution(String s){

        Stack<Character> stack = new Stack<>() ; 
        
        for(int i = 0 ; i < s.length(); i++){
            char character = s.charAt(i) ; 
            if(!stack.isEmpty() && stack.peek() == character)
                stack.pop() ; 
            else
                stack.push(character) ; 
        }
        return stack.isEmpty() ? 1 : 0 ; 
    }
}