class Solution {    
    int[][] dp ; 
    int n , m ; 
    
    public int solution(int[][] triangle) {
        n = triangle.length ; 
        m = triangle[n-1].length ; 
        dp = new int[n][m] ;
        
        // part 1. 초기 상태 채우기 
        dp[0][0] = triangle[0][0] ; // 꼭지점 
        
        // 왼쪽 변 & 오른쪽 변 
        for(int i = 1 ; i < n ; i++ ){
            dp[i][0] = dp[i-1][0] + triangle[i][0] ; 
        }
        for(int i = 1 ; i < n ; i++ ){ 
            int index = triangle[i].length -1 ; 
            dp[i][index] =  dp[i-1][index-1] + triangle[i][index] ;  
        }    
   
        // part 2. 점화식 (dp 배열 채우기)
        /*
        index 사이의 규칙 
        : 해당 숫자의 왼쪽 아래에 있는 숫자의 index는 서로 같고, 
          오른쪽 아래에 있는 숫자의 index는 1 크다 
          dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j] 
        */ 
        for(int i = 2 ; i < n ; i++ ){
            int index = triangle[i].length -1 ; 
            
            for(int j = 1 ; j < index ; j++ ){
                dp[i][j] 
                    = Math.max(dp[i-1][j-1]
                               , dp[i-1][j]) + triangle[i][j]; 
            }          
        }
            
        // part 3. 최댓값 도출 
        // dp[n][1~m] --> 최댓값
        int max =0 ; 
        for(int i = 0 ; i < m ; i++ ){
            max = Math.max(max, dp[n-1][i]) ; 
        }
        return max ; 
    } // solution
} // Solution