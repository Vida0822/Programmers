import java.util.* ; 
class Solution {
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
        bfs() ; 
          
        for(int i = 0 ; i < n ; i++){ //  visited.length -- IndexOutofRange : 300 으로 잡아놔서 
            if(!visited[i]){
                networks ++ ; 
                
                visited[i] = true ; 
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