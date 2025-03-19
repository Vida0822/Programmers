import java.util.* ; 
import java.io.* ; 

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ; 
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray() ;
        int N = input[0], C = input[1] ;  
        // 공유기 C개 
        // 가장 인접한 두 공유기 사이 '거리' : answer --> 최대로 설치 
        
        int[] houses = new int[N] ; 
        for(int i = 0 ; i < N ; i++){
            houses[i] = Integer.parseInt(br.readLine()) ; 
        }
        Arrays.sort(houses); 
        
        int left = 0, right = houses[N-1] - houses[0] ; 
        int answer = 0 ; 
        while(left <= right){
            int mid = (left+right) / 2 ; 
            
            if(canInstall(mid, houses, C)){
                answer = mid; 
                left = mid+1 ; 
            }else{
                right = mid-1 ;
            }
        }
        System.out.println(answer) ;   
    }
    
    public static boolean canInstall(int dist,int[] houses, int C){
        // 첫 집에는 무조건 공유기를 설치한다고 가정 
        int count = 1 ; 
        int prev = houses[0] ; 
        
        for(int i = 1 ; i < houses.length ; i++){
            if(houses[i] - prev >= dist){
                count++ ; 
                prev = houses[i] ; 
                if(count >= C)
                    return true ; 
            }
        }
        return false ;  
    }
}