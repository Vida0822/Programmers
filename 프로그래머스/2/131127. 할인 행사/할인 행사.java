import java.util.* ; 
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        
        Queue<String> q = new LinkedList<>() ;    
        HashMap<String, Integer> count = new HashMap<>() ;
        
        int answer = 0 ; 
        for(int i = 0 ; i < 10 ; i++){
            String sale = discount[i] ; 
            q.offer(discount[i]) ; 
            count.put(sale, count.getOrDefault(sale, 0)+1) ; 
        }
        if(allDiscounted(want,number,count))
            answer++ ; 
        
        // sliding window --> 
        // 1. 1day-,1day+ & count update    
        // 2. pullfill minimum count ? answer ++ 
        for(int i = 10 ; i < discount.length ; i++){
            String fDay = q.poll() ; 
            count.put(fDay, count.getOrDefault(fDay, 1) -1) ; 

            String lDay = discount[i] ; 
            q.offer(lDay) ; 
            count.put(lDay, count.getOrDefault(lDay, 0) +1) ; 
            
            if(allDiscounted(want, number, count))
                answer++ ; 
        }
        return answer ; 
    }
    
    public boolean allDiscounted(String[] want, int[] number, HashMap<String,Integer> count){
        for(int i = 0 ; i < want.length ; i++){
            String name = want[i] ; 
            int num = number[i] ; 
            
            if(num > count.getOrDefault(name, 0))
                return false ; 
        }
        return true ; 
    }
}