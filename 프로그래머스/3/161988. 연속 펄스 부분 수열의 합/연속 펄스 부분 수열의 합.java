class Solution {
    public long solution(int[] sequence) {
        // 수열, 합 중 최댓값 --> dp? 
        // n = 500000 --> O(NlogN) 이하  
        // 부분수열 1 : 1 시작 펄스수열 반영 -> dp : 그 중 최댓값 ? 
        // 부분수열 2 : -1 시작 펄스수열 반영 -> dp 
        long[] seq1 = new long[sequence.length] ; 
        long[] seq2 = new long[sequence.length] ; 
        
        int[] perse = {1, -1} ; 
        for(int i = 0 ; i < sequence.length ; i++){ // O(N)
            seq1[i] = sequence[i]*perse[(i+1)%2] ; 
            seq2[i] = sequence[i]*perse[i%2] ;
        }
        
        // 점화식 dp[i] = Math.max(dp[i-1]+dp[i] , dp[i]) 
        long answer = Math.max(seq1[0], seq2[0]) ;  
        for(int i = 1 ; i < sequence.length ; i++){ // O(N)
            seq1[i] = Math.max(seq1[i-1]+seq1[i] , seq1[i] ) ; 
            seq2[i] = Math.max(seq2[i-1]+seq2[i] , seq2[i] ) ; 
            answer = Math.max(answer, Math.max(seq1[i], seq2[i]) ); 
        }
        return answer ; 
    }
}