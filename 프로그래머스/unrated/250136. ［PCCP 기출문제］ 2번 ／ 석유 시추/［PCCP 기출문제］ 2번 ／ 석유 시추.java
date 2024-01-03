import java.util. * ; 

class Solution {
    
    int n, m ; // 행갯수, 열갯수 
    int[][] land ;  // 좌표당 석유 존재 여부를 담은 배열 (매개변수)
    int[][] oil ; // 좌표당 석유 덩어리의 ID를 저장하는 배열 
    boolean[][] visited ; // 석유 덩어리 크기 측정시 방문여부를 저장할 배열 
  
    public int solution(int[][] land) {
        this.land = land ; 
        this.n = land.length ;  
        this.m = land[0].length ; 
        
        this.oil = new int[n][m] ; 
        this.visited = new boolean[n][m] ; 
        
        // part 1. 모든 칸에 대해 BFS를 수행하여 석유 덩어리를 찾고, 그 크기를 각각 계산해서 저장 
        int oilId = 0 ;  // 석유 덩어리를 구분짓는 key값
        Map<Integer, Integer> oilSize = new HashMap<>() ; // 각 석유 덩어리의 크기를 저장하는 맵 
        
        for(int i = 0 ; i < n ; i++){
            // bfs 의 핵심 : 방문한 곳은 다시 방문하지 않아 효율성을 높임
            for(int j = 0 ; j < m ; j++){ // 매 좌표를 검사하면서 
                if(land[i][j] == 1 && !visited[i][j]) {
                    int size = bfs(i, j , oilId) ; // bfs 방식으로 덩어리 총량을 계산해 size 도출 (이 좌표와 인접한 애들은 다 같은 oilId 덩어리로 포함되고 방문처리됨)
                    oilSize.put(oilId, size) ;  // 해당 oilKey를 구분자로 Hashing 
                    oilId++ ; 
                }
            }// j 
        }// i 
        
        // part 2. 각 열마다 뽑을 수 있는 석유의 총량을 계산하여 저장
        int[] oilSum = new int[m] ;  // 각 열에서 뽑을 수 있는 석유의 총량 
        for(int j = 0 ; j < m ; j++){
            Set<Integer> oilSet = new HashSet<>() ; // oilId의 중복저장 방지 
            for(int i = 0 ; i < n ; i++){ // 각 열 별로 아래로 따라 내려감 
                if(land[i][j] == 1 ){
                    oilSet.add(oil[i][j]) ; // 각 좌표별 석유 덩어리의 key가 저장되어있는 oil 배열에서 oilId 값 가져옴 
                } // if 
            } // j 
            for(int key : oilSet){
                oilSum[j] += oilSize.get(key) ; // 그 key 값으로 각 oilId 별로 석유 덩어리의 크기가 저장되어있는 oilSize에서 value 값 가져옴  
            } // id 
        } // i 
        
        // part 3. 뽑을 수 있는 석유량 중 최대 도출
        return Arrays.stream(oilSum).max().getAsInt() ; // 배열 최대값 도출 좋은 로직 
  
    }  // solution 
    
    private int bfs(int x, int y , int oilId){
        // 주어진 좌표에서 bfs 방식으로 주변에 oil있는지 여부를 찾아내 누적
        Queue<int[]> queue = new LinkedList<>() ; 
        queue.offer(new int[]{x,y}) ; // 검사할 대기라인에 좌표 넣기 (이 시점엔 얘밖에 없지만 아래 반복문에서 이제 얘 뒤로 줄섬)
        visited[x][y] = true ; // 재검사 방지 위해 flag 
        oil[x][y] = oilId;  
        int size = 1 ; 
          
        int[] dx = {-1, 0, 1, 0} ; 
        int[] dy = {0, 1 , 0, -1} ; 
        
        while(!queue.isEmpty()){
            int[] current = queue.poll() ; // 줄 맨앞에부터 빼서 
            
            for(int i=0; i<4 ; i++){
                // 해당 좌표에 인접한 칸들 돌면서 
                int nx = current[0] + dx[i] ; 
                int ny = current[1] + dy[i] ; 
              
                if(nx >= 0 && nx < n && ny >= 0 && ny < m  // 좌표 범위를 벗어나지 않고 
                    && land[nx][ny] == 1  // 석유가 존재하며
                    && !visited[nx][ny]  // 방문하지 않은 좌표라면
                  ){ 
                    oil[nx][ny] = oilId; // 해당 좌표도 덩어리에 포함하고 
                    queue.offer(new int[]{nx,ny}) ; // 해당 좌표도 줄세우고 
                    visited[nx][ny] = true ;  // 방문처리 
                    size++;  // size 누적                    
                } // if 
            } // i            
        }// while 
        return size ; 
    } // bfs 
} // class 