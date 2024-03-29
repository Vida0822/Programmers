import java.util.* ; 
class Solution {
    public int solution(int[] elements) {
        // dp 
        HashSet<Integer> nums = new HashSet<>() ; 
        int n = elements.length; 
        
        for(int i = 0 ; i < n ; i++){
            // sliding window 
            int sum = 0 ; 
            for(int j = 0 ; j < i ; j++){
                sum += elements[j] ; 
                nums.add(sum) ; 
            }
            for(int j = 0 ; j < n ; j++){
                sum -= elements[j] ; 
                sum += elements[(j+i >= n? j+i-n : j+i)] ; 
                nums.add(sum) ; 
            }
        }
        return nums.size() ; 
    }
}