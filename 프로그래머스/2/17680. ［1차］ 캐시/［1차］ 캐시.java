import java.util.*; 
class Solution {
    public int solution(int cacheSize, String[] cities) {
        
        // 특정 size를 넘어가면 맨 처음 넌거 out --> Queue? HashSet? 
        Queue<String> q = new LinkedList<>() ; 
        HashSet<String> set = new HashSet<>() ; 
        
        int answer = 0 ; 
        for(int i = 0 ; i < cities.length ; i++){
            String city = cities[i] ;  
            city = city.toUpperCase(); 
            
            if(set.contains(city)){
                answer += 1; 
                q.remove(city) ; 
            }
            // 큐에 새로 담아주는 작업 필요 
            
            else{ // jeju Seoul jeju
                answer+=5; 
                set.add(city) ;  
            }
            q.add(city) ;  
            if(q.size() > cacheSize)
                set.remove(q.poll()) ;       
        }
        // 일부 테케 통과 x -> 경계값 분석 (극단적인 입력값을 검사한다)
        // 캐시크기가 0 
        return answer;
    }
}