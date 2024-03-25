import java.util.* ; 
class Node implements Comparable<Node>{
    int index ; // 도착 노드 
    int cost ; // 비용 
    
    public Node(int index, int cost){
        this.index = index ;
        this.cost = cost ; 
    }
    
    @Override
    public int compareTo(Node other){
        return this.cost - other.cost ; 
    }
}

class Solution {
    public static ArrayList<ArrayList<Node>> graph ; 
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        // 최단거리 --> 가중치가 있는 양방향 그래프 
        // 그래프 만들기 
        graph = new ArrayList<>() ; 
        for(int i = 0 ; i <= n ; i++){
            graph.add(new ArrayList<>()) ; 
        }
        for(int i = 0 ; i < fares.length ; i++){
            graph.get(fares[i][0]).add(new Node(fares[i][1], fares[i][2])) ; 
            graph.get(fares[i][1]).add(new Node(fares[i][0], fares[i][2])) ; 
        }
        
        int[] startA = dijkstra(a, n) ; 
        int[] startB = dijkstra(b, n) ; 
        int[] start = dijkstra(s, n) ; 
    
        int answer = 200000001; 
        for(int i = 1 ; i <= n ; i++){
            answer = Math.min(answer , 
                             start[i] + startA[i] + startB[i]) ; 
        }
        return answer ; 
    }
    
    public int[] dijkstra(int start, int n){
        int[] d = new int[n+1] ;  // d[i] : start -> i 까지의 거리 
        Arrays.fill(d, 20000001) ; 
        PriorityQueue<Node> pq = new PriorityQueue<>() ; 
        pq.offer(new Node(start, 0)); 
        d[start] = 0 ; 
        
        while(!pq.isEmpty()){
            Node now = pq.poll() ; 
            
            for(Node next : graph.get(now.index)){
                int cost = d[now.index]+next.cost; 
                if(cost < d[next.index]){
                    d[next.index] = cost ; 
                    pq.offer(new Node(next.index, cost)) ; 
                }
            }
        }
        return d; 
    }
}