class Solution {
    public long solution(int n) {
        
        if(n <= 1)
            return 1; 
        // dp 사용 
        long[] dp = new long[n] ; 
        dp[0] = 1 ;
        dp[1] = 2 ; 
        // 1 2 3  
        for(int i = 2 ; i < n ;i++){
            dp[i] = (dp[i-2] + dp[i-1]) % 1234567 ;      
        }
        return dp[n-1] ; 
        
        // 두번째칸까지 갈수있는 방법 : 2가지 (1,1) (2)
        // 세번째 칸까리 갈수있는 방법 : 전전칸에서 두칸 점프 + 전칸에서 한칸 이동 (이때 전전칸에선 반드시 2칸 점프해야함, 한칸한칸 하면 전칸에서 한칸 점프 경우랑 겹치기 때문에 중복으로 더해짐)
        
    }
}