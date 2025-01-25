class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        
        int max = 0 ;
        for(int i = 0 ; i < diffs.length ; i++){
            max = Math.max(max,diffs[i]);
        }
        int left = 0 , right = max; 
        while(left <= right){
            int mid = (left+right)/2 ;
            // System.out.println("mid = "+mid);
            if(isPossible(diffs, times, limit, mid)){
                answer = mid ; 
                right = mid - 1 ;
            }else{
                left = mid + 1 ; 
            }
            
        }
        return answer ;
    }
    /*
    해당 숙련도로 퍼즐 푸는 시간 계산
    */
    public static boolean isPossible(int[] diffs, int[] times, long limit, int level){
        if(level <= 0)
            return false; 
        long total = times[0] ;
        for(int i = 1 ; i < diffs.length ; i++){
            int diff = diffs[i] ;
            int time_cur = times[i] ; 
            
            if(diff <= level){
                total += time_cur ;
            }else{
                long t = (times[i-1] + time_cur)*(diff - level) + time_cur ; 
               // System.out.println("t = "+t);
                total += t ;
            }
        }
        //System.out.println("level = "+level);
        //System.out.println("time_prev = "+total);
        if(total <= limit)
            return true;
        else
            return false;
    }
}