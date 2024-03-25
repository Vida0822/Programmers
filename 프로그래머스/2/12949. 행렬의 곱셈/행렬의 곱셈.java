class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int n = arr1.length ; 
        int m = arr2[0].length ; 
        
        int[][] answer = new int[n][m] ; 
        for(int i = 0 ; i < n ; i++){ // 1 
            for(int j = 0 ; j < m ; j++){ // 0 ~ 2 
                answer[i][j] = getResult(arr1, arr2, i, j) ; 
            }
        }
        return answer ; 
    }
    
    public int getResult(int[][] arr1, int[][] arr2, int row, int col){
        int sum = 0 ; 
        for(int i = 0 ; i < arr1[0].length ; i++){
            sum += (arr1[row][i] * arr2[i][col]) ; 
        }
        return sum ; 
    }
}