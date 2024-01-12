import java.util.* ; 
class Solution {
    
    /*
    1. bfs 를 활용한 풀이 
    */
    static boolean[] visited = new boolean[300] ; 
    static Queue<Integer> q = new LinkedList<Integer>() ; 
    public static int n ; 
    public static int[][] computers ; 
    
    public int solution(int n, int[][] computers) {

        // n - vertex : 정점 (출발) , currV : 현재 검사 위치 (도착)
        int networks = 0 ;       
        this.n = n ; 
        this.computers = computers; 
        
        q.add(0) ; 
        visited[0] = true ;
        networks ++ ; 
        
        // 0번 컴퓨터와 한 네트워크에 연결된 컴퓨터들을 순회한다  
        bfs() ; 
          
        // 0번 컴퓨터 네트워크에 대한 검사를 마친후, 방문하지 않은 컴퓨터들이 있는지 하나씩 검사한다
        for(int i = 0 ; i < n ; i++){ //  visited.length -- IndexOutofRange : 300 으로 잡아놔서 
            
            // 만약 방문하지 않은 컴퓨터가 있다면 별개의 네트워크! 
            if(!visited[i]){
                networks ++ ; // 네트워크 갯수 추가     
                visited[i] = true ; 
               
                // 해당 컴퓨터를 기준으로 연결된 컴퓨터들을 순회한다  
                q.add(i) ; // 여기에 164 들어가면 computers에서 걸림 ! 
                bfs() ; 
            }
        } // for 
        return networks ; 
    } // main 
    
    public void bfs(){
         while(!q.isEmpty()){
            int vertex = q.poll() ; 
            for(int currV = 0 ; currV < n ; currV++){
                if(computers[vertex][currV] == 1 && !visited[currV] ){
                    visited[currV]  = true ; 
                    q.add(currV) ; 
                }
            } // for
        }  // while 
    } // bfs 
} // class
/*
class Solution{
    public int solution(int n , int[][ computers]){
        int answer = 0 ; 
        boolean[] visited = new boolean[n] ; 
        for(int i = 0 ; i < n ; i++){
            if(!visited[i]){
                // dfs 를 다하고 빠져나왔는데 방문안한 노드가 있으면 다른 네트워크 --> 해당 노드로 다시 네트워크 탐색
                dfs(computers, chk, i) ; 
                answer++ ; 
            }
        }
        return answer ; 
    }
    void dfs(int[][] computers, boolean[] visited, int start){
        visited[start] = true ;  // visited 바꿔주는 코드를 처음에 포함하는게 간결해짐 
        for(int i = 0 ; i < computers.length ; i++){
            if(computers[start][i] == 1 && !visited[i]){
                dfs(computers, visited, i) ; 
            }
        }
    } 
}
*/