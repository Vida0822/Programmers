import java.util.*  ; 
class Node implements Comparable<Node>{
	int index ; 
	int distance ; 

    public Node(int index, int distance){
        this.index = index ; 
        this.distance = distance ; 
    }
	@Override
	public int compareTo(Node other) {
		// 음수가 나오면 this가 우선 
		if(this.distance < other.distance) {
			return -1 ; 
		}
		return 1 ; 
	}
} // Node 

class Solution {
    public static int INF = (int)1e9; 
    public static int n ; 
    public static int[] d ; 
    public static ArrayList<ArrayList<Node>> graph = new ArrayList<>() ; 
    
    public int solution(int n, int[][] edge) {
        this.n = n ; 
        this.d = new int[n + 1];
        // ArrayList형 그래프 만들고 
        for(int i = 0; i <=n ; i++){
            graph.add(new ArrayList<>()) ; 
        }
        for(int i = 0 ; i < edge.length ; i++){
            int from = edge[i][0] ; 
            int to = edge[i][1] ; 
            graph.get(from).add(new Node(to, 1)); // 수정된 부분
            graph.get(to).add(new Node(from, 1)); // 수정된 부분

        }
        Arrays.fill(d, INF); 
        
        // 다익스트라 수행 
        dikstra(1) ;
        
        // 최단거리 배열에서 가장 큰 값을 가진 노드들 반환
        int max = 0 ; 
        for(int i = 1 ; i <= n ; i++ ){
            if(d[i] < INF){
                System.out.print(d[i]+" ") ; 
                max = Math.max(max, d[i]) ; 
            }
        }
        int answer = 0; 
        for(int i = 1 ; i <= n ; i++ ){
            if(d[i] == max){
                answer++; 
            }
        }
        return answer; 
    }
    
    public static void dikstra(int start){
        PriorityQueue<Node> pq = new PriorityQueue<>(); 
        pq.offer(new Node(start,0)) ; 
        d[start] = 0 ; 
        
        while(!pq.isEmpty()){
            Node node = pq.poll() ; 
            int now = node.index ; 
            int dist = node.distance ; 
            
            if(d[now] < dist)  // 1 
                continue ; 
            
            for(Node nextNode:graph.get(now)){
                int cost = d[now] + nextNode.distance ; 
                if(cost < d[nextNode.index]){
                    d[nextNode.index] = cost ; 
                    pq.offer(new Node(nextNode.index, cost)) ; 
                } // if 
            } // for 
        } // while 
    }
}