class Solution {
    public String solution(int n, int t, int m, int p) {
        
        int index = 1 ; 
        String answer  = "" ; 
            
        a : for(int num = 0 ; num < t*m ; num++){
            // 1. 각 숫자 n진수로 변환 
            String converted_num = toNDecimal(n, num) ;
             
            for(int i = 0 ; i < converted_num.length() ; i++){
                // 2. 한글자씩 말하면서
                        
                // 3. 만약 무지의 차례면 자기 숫자에 추가  
                if(index == p){
                    answer += converted_num.charAt(i) ;  
                    if(answer.length() == t) break a; 
                    p += m ;
                }
                index++ ; 
            } 
        }
        return answer ; 
    }
    public static String toNDecimal(int n, int num){
        String result = "" ; 
        
        if(num == 0 || num == 1)
            return num+"" ; 
        
        while(num != 0){
            int turn = num % n ; 
            
            if(n > 10 && turn > 9){
                result = toAlpa(turn) + result ; 
            }else{
                result = turn + result ; 
            }
            num /= n; 
        }
        return result ; 
    }
    
    public static char toAlpa(int turn){
        switch(turn){
            case 10 : 
                turn = 'A' ; 
                break ; 
            case 11 : 
                turn = 'B' ; 
                break ; 
            case 12 : 
                turn = 'C' ; 
                break ; 
            case 13 : 
                turn = 'D' ; 
                break ; 
            case 14 : 
                turn = 'E' ; 
                break ; 
            case 15 : 
                turn = 'F' ; 
                break ; 
        }      
        return (char)turn ; 
    }
}