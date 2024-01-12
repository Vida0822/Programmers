import java.util.* ; 
class Solution {
    boolean solution(String s) {
        /*
        [스택을 사용한 풀이]
        (가 '먼저' 들어가야하며, (가 들어가면 반드시 동일한 갯수의 )가 나와야한다 
        => (가 나오면 스택에 쌓고 )가 나오면 스택에서 빼서 최송적으로 스택이 비어있으면 true를 return 
        */
        Stack stack = new Stack() ; 
        for(int i = 0 ; i < s.length() ; i++){
            char c = s.charAt(i) ; // 문자열을 한글자씩 검사하면서 
            if(c == '('){ // (가 나오면 스택에 쌓고 
                stack.push(c) ; 
            }else{ // ) 가 나왔는데, 
                if(stack.size() == 0)  
                    // stack size가 0인데 ')'가 나온 경우는 이미 잘못된 경우이다 
                    return false ; 
                stack.pop() ; 
            }
        }
        return stack.size()==0?true:false ; // 스택이 비어있으면 올바른 괄호사용이다
    }
}