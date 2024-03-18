import java.util.*; 
class Solution {
    public int solution(int[] people, int limit) {
        // 정렬 
        Arrays.sort(people) ; 
        
        // greedy 알고리즘 --> 정확히 최적을 맞추기 위해 큰 몸무게 + 작은 몸무게 조합을 구한다 
        int answer = 0 ; 
        int left = 0 , right = people.length-1; 
        while(left<=right){
            if(people[left]+people[right] <= limit){
                left++ ; 
            }
            right--  ;
            answer++; 
        }
        return answer ;  // 10 20 30 40 50 
                                                    
        
    }
}