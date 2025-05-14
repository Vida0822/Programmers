import java.util.* ; 
import java.io.* ;

class Solution{
    public static void main(String[] args) throws IOException{   
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ;
        for(int t = 1 ; t <= 10 ; t++){
        	
            int N = Integer.parseInt(br.readLine()) ;
        	int[] builds =Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray()   ; 

        	int answer = 0; 
        	for(int i = 2 ; i < N - 2 ; i++){
            	int height = builds[i]; 
            	int max = Math.max(Math.max(builds[i-2], builds[i-1]), Math.max(builds[i+1], builds[i+2])); 
            	if(height > max)
                	answer += height - max ; 
        	}
        	System.out.println("#"+t+" "+answer);
		}
    }
}
