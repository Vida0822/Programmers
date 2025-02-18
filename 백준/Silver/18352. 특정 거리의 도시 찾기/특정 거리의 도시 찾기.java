import java.util.* ; 
import java.io.* ; 

class Main{
    public static void main(String[] args) throws IOException{
        // 도시 X -> 모든 도시로의 최단거리 
        // 정확히 K 인 도시 번호들
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ; 
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray() ; 
        int N = input[0], M = input[1], K = input[2], X = input[3] ;
        
        // 그래프 생성 : ArrayList
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>() ; 
        for(int i = 0 ; i < N+1 ; i++){ // O(N)
            graph.add(new ArrayList()) ;             
        }
        for(int i = 0 ; i < M ; i++){ // O(M)
            int[] input2 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray() ; 
            graph.get(input2[0]).add(input2[1]) ; 
        }
        Arrays.stream(bfs(graph,K,X).split(" ")).forEach(city -> System.out.println(city)) ;    
    }
    
    public static String bfs(ArrayList<ArrayList<Integer>> graph, int K, int X){
        int[] distances = new int[graph.size()]; 
        Arrays.fill(distances, -1) ; 
        distances[X] = 0 ;
        
        Queue<Integer> q = new LinkedList<>() ; 
        q.offer(X) ; 
        
        while(!q.isEmpty()){ // O(NlogN)
            int start = q.poll() ; 
            
            for(Integer end : graph.get(start)){
                // if(distances[end] <= start.distance+1) --> X : 가장 가까운 지점만 선택하는 bfs에서 선택된 Node는 도시 X에서 무조건 최단거리! 재갱신 필요없다    
                if(distances[end] == -1){ // 방문X 도시라면
                    distances[end] = distances[start]+1;   // ****
                    q.offer(end) ; 
                }
            }
        }
        
        StringBuilder answer = new StringBuilder() ; 
        for(int i = 1 ; i < distances.length ; i++){
            if(distances[i]==K)
                answer.append(i).append(" ") ; 
        }
        if(answer.length()==0)
            return "-1" ;  
        return answer.toString() ; 
     }
}