import java.util.*; 
class Solution {
    public int solution(int k, int[] tangerine) {
        // minimize the number of types of mandarine
        // greedy : choose the most large number of counts of the weight 
        
        // return the number of types of mandarine
        // map ? class ? : HashSet <-- (weight)
        Arrays.sort(tangerine) ; 
        HashMap<Integer, Integer> map = new HashMap<>() ; 
        for(int i = 0 ; i < tangerine.length ; i++){
            int weight = tangerine[i] ; 
            map.put(weight, map.getOrDefault(weight, 0)+1) ; 
        }
        
        List<Integer> values = new ArrayList(map.values()) ; // don't neet weight information
        Collections.sort(values, Comparator.reverseOrder()) ; // greedy 
        
        int answer = 0 ; 
        for(int count : values){ // greedy
            answer++ ; 
            k -= count ; 
            if(k <= 0)
                break ; 
        }
        return answer ; 
        
    }
}