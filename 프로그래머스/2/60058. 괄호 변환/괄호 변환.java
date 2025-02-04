import java.util.*;

class Solution {
    public String solution(String p) {
        // 문제 : 괄호 개수는 맞지만 짝이 안맞음
        // 메서드 1 : '올바른 괄호'인지 체크
        // 메서드 2 : '올바른 괄호'로 변환
        if(check(p)){
            return p; 
        }else{
            return correct(p);
        }
    }
    
    public boolean check(String p){ // 재귀함수
        
        if(p.length()==0)
            return true; 
        
        Stack<String> s = new Stack() ;
        for(int i = 0 ; i < p.length() ; i++){
            
            if(p.charAt(i)=='('){
                s.push(p.charAt(i)+"");
            }else{
                try{
                    s.peek();
                }catch(Exception e){
                    return false;
                }
                s.pop();
            }            
        }
        if(s.size()==0)
            return true ;
        return false ;
    } // check()
    
    public String correct(String p){
        
        if(p.length()==0)
            return p ;
        
        int index = find(p) ;
        String u = p.substring(0,index+1);
        String v = "" ;
        if(index < p.length()-1)
            v = p.substring(index+1);
        
        if(check(u)){
            v = correct(v) ;
            return u + v ;
        }else{
            v = "(" + correct(v) + ")" ; 
            u = reverse(u);
            return v + u;
        }
    } // correct()
    
    public int find(String p){
        int t = 0;
        for(int i = 0 ; i < p.length() ; i++){
            
            if(p.charAt(i) == '('){
                t+=1;
            }else{
                t-=1;
            } 
            if(t==0)
                return i ;
        }
        return p.length();
    } // find()
    
    public String reverse(String u){
        if(u.length() < 3)
            return ""; 
        
        u = u.substring(1,u.length()-1) ;
            
        String ret = "";
        for(int i = 0 ; i < u.length() ; i++){
            if(u.charAt(i)=='(')
                ret+=")";
            else
                ret+="(";
        }
        return ret;
    } // reverse()
}