import java.util.* ; 
import java.io.* ; 

class Main{
    public static void main(String[] args) throws IOException{
        // 최대한 적은 개수의 연속된 숫자부분을 찾아서 뒤집기 
        // 0과 1중 연속숫자묶음 개수가 작은 쪽을 반환 
        // S의 길이 : 100만 --> 최대한 효율적인 : O(N)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ;
        String S = br.readLine() ; 
        
        int zero = 0 , one = 0 ; 
        char prevChar  = '\0'; 
        for(char c : S.toCharArray()){
            if(c != prevChar){
                if(c == '0') {
                    zero++; 
                }else{
                    one++ ; 
                }
            }
            prevChar = c ; 
        }
        
        System.out.println(Math.min(zero, one)) ;         
    }
}