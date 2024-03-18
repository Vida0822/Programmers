import java.util.* ; 
class Solution {
    public int[] solution(int n, long left, long right) {
        // n = 10^7 --> 굉장히 크다 ... 순차탐색은 안되겠군 --> 규칙성을 찾는게 중요 
        // 1행 : 1 ~ n 
        // 2행 : 2(2개) ~ n 
        // 3행 : 3(3개) ~ n 
        // 4행 : 4(4개) ~ n 
        // n행 : n(n개)
        // + 모든 배열을 다 채울 필요 없이 left ~ right안의 행만 채우면됨 
        // 행 --> left / n , 열 --> left % n 
        // ~ 행 --> right / n , 열 --> right % n 
        // 최악의 경우 O(N^2)
        ArrayList<Integer> nums = new ArrayList<>(); 
        long startRow = left/n+1; // 1 ~ n 
        long endRow = right/n+1; // 1 ~ n 
        
        for(long i = startRow; i <= endRow ;i++){ 
            // ex) 2행 3열 ~ 5행 5열
            for(int j = 1 ; j <= n ; j++){
                
                if((i-1)*n+j -1 < left) 
                    continue  ; 
                if((i-1)*n+j -1 > right)
                    break ;
                          
                if(j <= i)
                    nums.add((int)i) ; 
                else
                    nums.add(j) ;             
            }
        }
        
        // 답 변환 
        int diff = (int)(right-left) ; 
        int[] answer = new int[diff+1] ; 
        for(int i = 0 ; i < nums.size() ; i++){
            answer[i] = nums.get(i) ; 
        }
        return answer; 
    }
}