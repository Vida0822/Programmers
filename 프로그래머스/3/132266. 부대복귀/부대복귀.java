import java.util.*;

class Solution {
    private static List<List<Integer>> graph;
    private static int[] dist;
    private static final int MAX = 1_000_000_000;

    public static int[] solution(int n, int[][] roads, int[] sources, int destination) {

        graph = new ArrayList<>();
        for(int i=0; i<n+1; i++) graph.add(new ArrayList<>());

        for (int[] road : roads) {
            int s = road[0];
            int e = road[1];

            graph.get(s).add(e);
            graph.get(e).add(s);
        }

        dist = new int[n+1];
        Arrays.fill(dist, MAX);
        dijkstra(destination);

        int[] answer = new int[sources.length];
        for (int i = 0; i < sources.length; i++) {
            answer[i] = (dist[sources[i]] < MAX) ? dist[sources[i]] : -1;
        }
        return answer;
    }

    private static void dijkstra(int departure) {
        Queue<Integer> q = new LinkedList<>() ; 
        // 가중치가 없을땐 우선순위 큐와 Node 클래스를 따로 정의해줄 필요 없이 정수값(1)씩 누적한다
        q.add(departure); 
        dist[departure] = 0 ; 
        
        while(!q.isEmpty()){
            int cur = q.poll() ; 
            
            for(int i = 0 ; i < graph.get(cur).size() ;i++){
                int next = graph.get(cur).get(i) ; 
                if(dist[next] > dist[cur] + 1){
                    dist[next] = dist[cur]+1 ; 
                    q.add(next) ; 
                }
            } // for
        } // while
    } // dijkstra
}