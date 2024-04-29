import java.util.* ; 

class Pair implements Comparable<Pair>{
    int x ;
    int y ;
    int dist ; 
    
    public Pair(int x, int y, int dist){
        this.x = x ; 
        this.y = y ; 
        this.dist = dist ; 
    }
    
    @Override
    public int compareTo(Pair other){
        return this.dist - other.dist ; 
    }
}

class Solution {
    public static int n , m ; 
    
    public int solution(int[][] maps) {
        n = maps.length ; 
        m = maps[0].length ; 
        
        if(n != 1 && m != 1 && maps[n-2][m-1] == 0 && maps[n-1][m-2] == 0)
            return -1 ;
        
        // 최단거리 --> bfs 
        return bfs(maps, new Pair(0,0,1)) ; 
    }
    
    public static int bfs(int[][] maps, Pair start){
        
        int[][] dp = new int[n][m] ; 
        for(int i = 0 ; i < dp.length ; i++){
            Arrays.fill(dp[i], 10000) ; 
        }
        
        int[] dx = {-1, 1, 0, 0} ; 
        int[] dy = {0, 0, -1, 1} ; 
        
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>() ; 
        pq.add(start) ; 
        while(!pq.isEmpty()){
            Pair cur = pq.poll() ; 
            if(cur.x == n-1 && cur.y == m-1)
                return Math.min(dp[cur.x][cur.y], cur.dist) ;

            for(int i = 0 ; i < 4 ; i++){
                int nx = cur.x + dx[i] ;
                int ny = cur.y + dy[i] ; 
                
                if(nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue ; 
                if(maps[nx][ny] == 0)
                    continue ; 
                if(cur.dist + 1 < dp[nx][ny]){
                    pq.add(new Pair(nx, ny, cur.dist+1)) ; 
                    dp[nx][ny] = cur.dist + 1; 
                }
            }
        }
        return -1; 
    }
}