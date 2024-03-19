import java.util.* ; 
class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        
        // 대기열 (전체인원)
        PriorityQueue<Integer> pq = new PriorityQueue<>() ; 
        for(String table:timetable){
            int time = Integer.parseInt(table.substring(0,2))*60 + Integer.parseInt(table.substring(3));
            pq.add(time);
        }
        
        int startTime = 9*60 ;
        int lastTime = 0 ; 
        int count = 0; 
        for(int i = 0 ; i < n ; i++){
            count = 0 ; 
            while(!pq.isEmpty()){
                int boardTime = pq.peek() ; 
                if(boardTime <= startTime && count < m){
                    pq.poll() ;
                    count++ ; 
                }else{
                    break ; 
                }
                lastTime = boardTime-1 ; // last member' boarding time -1
            }
            startTime += t; 
        }
        if(count < m) 
            lastTime = startTime-t ; // in the end of loop, added t to last bus time
        
        return String.format("%02d:%02d", lastTime/60, lastTime%60) ; 
        
    }
}