import java.util.* ; 

class Solution {
    HashMap<Long, Long> m = new HashMap<>() ;
    
    public long[] solution(long k, long[] room_number) {
        
        
        long[] answer = new long[room_number.length] ; 
        for(int i = 0 ; i < room_number.length ; i++){
            answer[i] = matchRoom(room_number[i]) ; 
        }
        return answer ; 
    }  
    
    // 요청한 방번호(reqRnum)에 대해 실제로 배정된 방 번호(resRnum)를 return 하는 함수 
    public long matchRoom(long reqRnum){ 
        long resRnum = reqRnum ; 
        
        // <4 , 6>  --> 6번방은 비어있는지 다시 확인(재귀) 
        if(m.containsKey(reqRnum))
            resRnum = matchRoom(m.get(reqRnum)) ; 
        
        m.put(reqRnum, resRnum + 1);  
        return resRnum ; 
    } // matchRoom
    
     
        /*
        long[] answer = new long[room_number.length] ; 
        TreeSet<Long> s = new TreeSet<>() ;
               
        for(long i = 1 ; i <= k ; i ++){
            s.add(i) ; 
        }      
        for(int i = 0 ; i < room_number.length ; i++){
            answer[i]  = s.ceiling(room_number[i]) ;   // 탐색          
            s.remove(answer[i]) ; // remove 후 정렬 
        }
        return answer; 
        */ 
    
}