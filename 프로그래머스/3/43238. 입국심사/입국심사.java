import java.util.* ; 
class Solution {
    public long solution(int n, int[] times) {
        
        Arrays.sort(times) ; 
       
        long answer = 0 ; 
        long left = 0 , right = times[0] * (long) n  ; 
        while(left <= right){
            long mid = (left + right) / 2 ;             
            if(isPossible(n,times,mid)){
                answer = mid ; 
                right = mid -1 ; 
            }else
                left = mid + 1; 
        }
        return answer ; 
    }
    
    // ** 비즈니스 로직 ** : 해당 시간안에 n 명 모두 심사 가능 ? 
    public boolean isPossible(int n, int[] times, long maxMinutes){
        long complete = 0 ; 
        for(int i = 0 ; i < times.length ; i ++) {
			complete += maxMinutes/ times[i] ; // ** 
		}
        if(complete < n)
            return false ;
        return true ; 
    }
}