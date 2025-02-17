import java.util.* ; 
import java.io.* ; 

class Main  {  
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ; 
        String N = br.readLine() ; 
        
        System.out.println(canUse(N)? "LUCKY":"READY") ; 
    }
    
    public static boolean canUse(String N){ // N < 99,999,999 --> O(N^2) 미만 

        int len = N.length() ; 
        
        int sumA = 0, sumB = 0 ; 
        for(int i = 0 ; i < len/2 ; i++){
            sumA += Integer.parseInt(N.substring(i,i+1)) ; 
            sumB += Integer.parseInt(N.substring(i+len/2,i+len/2+1)) ; 
        }
        if(sumA==sumB)
            return true ; 
        else
            return false ;        
    }
}