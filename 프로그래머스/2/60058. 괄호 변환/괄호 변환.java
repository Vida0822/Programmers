import java.util.* ; 
class Solution {
    public String solution(String p) {
        // 재귀적으로 수행 (dfs 예상) -  2 이상 1,000 이하 : 작은 데이터값 
        // 1. u, v로 분리 - u기준 : 괄호 갯수 조건 일치하는 부분까지 u로 포함 
        // 2. 올바른 괄호인지 확인 + 올바른 괄호로 변환하고 result 문자열에 누적 
        // 3. v에 대해 1단계부터 다시 재귀적으로 수행 (v가 검사할 문자열인 p로써 기능)
        
        return dfs(p) ; 
    }
    public String dfs(String p){
        String result = "" ; 
        
        // 종료조건
        if(p.length() == 0)
            return p ; 
        
        // u, v 분리  
        String u = "" , v = ""; 
        int left = 0, right = 0 ; 
        
        for(int i = 0 ; i < p.length() ; i++){
            char c = p.charAt(i) ; 
        
            if(c == '('){
                left++ ;  
                u += c ; 
            }else{
                right++ ; 
                u += c ; 
            }
            if(left == right && i != p.length()-1) {
                v = p.substring(i+1) ; 
                break; 
            }
        }
        System.out.println("u:"+u);
        System.out.println("v:"+ v) ; 
        
        
        // u가 올바른 괄호인지 확인  
        if(rightExp(u)) 
            result +=  u + dfs(v) ; 
        else{
        // 올바른 괄호가 아니라면 올바른 괄호로 변환
            result += "(" + dfs(v) +")"; 
            for(int i = 1 ; i < u.length()-1 ; i++){
                char c = u.charAt(i) ; 
                if(c == '(')
                    result += ")" ; 
                else 
                    result += "(" ; 
            }
        }        
        return result ; 
    }
    
    public boolean rightExp(String u){
        Stack<Character> stack = new Stack<>() ; 
        for(int i = 0 ; i < u.length() ; i++){
            char c = u.charAt(i) ; 
            if(c == ')' ){
                if(stack.isEmpty()) return false ; 
                else  stack.pop() ; 
            }  
            else 
                stack.push(c) ; 
        }
        return stack.size() == 0 ? true : false ;
    }
}