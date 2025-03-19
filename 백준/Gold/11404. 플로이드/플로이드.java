import java.util.* ; 
import java.io.* ; 

class Main{
    public static final int INF = (int)1e9 ; 
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ; 
        int N = Integer.parseInt(br.readLine()), M = Integer.parseInt(br.readLine()) ;
        
        int[][] graph = new int[N+1][N+1] ; 
        for(int i = 1 ; i <= N ; i++){
            for(int j = 1 ; j <= N ; j++){
                if(i == j)
                    continue ;  // 0  
                graph[i][j] = INF ; // Integer.MAX_VALUE ; --> 밑에 더하는 부분에서 오버플로우 발생(음수값 도출되어 갱신)
            }
        }
        
        for(int i = 0 ; i < M ; i++){
            int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray() ; 
            graph[input[0]][input[1]] = Math.min(graph[input[0]][input[1]], input[2]) ; 
        }
        
        // 플로이드 워셜 알고리즘 : i와 j로 가는 경로 중 k를 거쳐가는 모든 경우의 수 
        for(int k = 1 ; k <= N ; k++){
            for(int i = 1 ; i <= N ; i++){
                for(int j = 1 ; j <= N ; j++){
                    graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]) ; 
                }
            }
        }
        
        for(int i = 1 ; i <= N ; i++){
            for(int j = 1 ; j <= N ; j++){
                System.out.print(graph[i][j] == INF? 0 : graph[i][j]) ; 
                System.out.print(" ");
            }
            System.out.println() ; 
        }
    }
}