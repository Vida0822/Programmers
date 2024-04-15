class Solution {
    public static int answer = 0; 
    
    public int solution(int[] numbers, int target) {
        // 연산자 끼워넣기 
        String[] operators = new String[numbers.length] ; 
        dfs(numbers, target, 0, operators) ; 
        
        return answer ; 
    }
    
    public static void dfs(int[] numbers, int target , int depth, String[] operators){
        if(depth == numbers.length ){
            if(isPossible(numbers, target, operators )) 
                answer ++ ; 
            return ; 
        }
        operators[depth] = "+" ; 
        dfs(numbers, target, depth+1 , operators) ; 
        operators[depth] = "-" ; 
        dfs(numbers, target, depth+1 , operators) ;
        return ; 
    }
    
    public static boolean isPossible(int[] numbers, int target , String[] operators){
        int sum = 0 ; 
        for(int i = 0 ; i < numbers.length ; i++){
            if(operators[i] == "+")
                sum += numbers[i] ; 
            else 
                sum -= numbers[i] ;
        }
        return sum == target ; 
    }
}