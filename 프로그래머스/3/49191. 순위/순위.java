class Solution {
    public int solution(int n, int[][] results) {
        // 플로이드 워셜 
        // 나보다 순위가 높은 사람 수 + 나보다 순위가 낮은 사람수 = n-1명이면 내 순위를 알 수 있다 
        // 즉 나로 이동 가능한 노드수 + 내가 이동 가능한 노드수 = n-1인지 확인
        // 진쪽 -> 이긴쪽 
        // 2 --> 3 
        // 2 --> 4 
        // 2 --> 1 
        // 플로이드 워셜 알고리즘
        // 그래프 만들기 
        
        
        int[][] graph = new int[n+1][n+1] ; 
        for(int i = 0 ; i < results.length ;i++){
            int win = results[i][0] ; 
            int lose = results[i][1] ; 
            graph[win][lose] = 1 ; 
            graph[lose][win] = -1 ; // 1 과 -1은 대칭으로 놓여진다
        }
        // 출발 
        for(int i = 1 ; i <= n;i++){
            // 도착 
            for(int j = 1 ; j <= n ; j++){
                // 거쳐감 
                for(int k = 1 ; k <= n ; k++){ 
                    if(graph[i][k] == 1 && graph[k][j] == 1 ){
                        graph[i][j] = 1;
                        graph[j][i] = -1 ; // ** 승자가 정해지면 패자도 정해진다  
                    }
                         
                    if(graph[i][k] == -1 && graph[k][j] == -1){
                        graph[i][j] = -1 ; 
                        graph[j][i] = 1 ; // 출력 해봤으면 바로 알문제
                    }
                }
            }
        }
        
        int answer = 0 ; 
        for(int i = 1 ; i <= n ; i++){
            int count = 0; 
            for(int j = 1 ; j <= n ; j++){
                if(graph[j][i] != 0 )
                    count++; 
            }
            if(count == n-1) 
                answer++; 
        }
        return answer ; 
    }
}