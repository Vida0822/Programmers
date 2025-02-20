import java.util.* ; 
import java.io.* ;

class Main{
    public static int N, M; 
    public static int max = 0; 

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray() ;
        N = input[0] ; // < 8
        M = input[1] ;
        
        int[][] lab = new int[N][M] ; 
        for(int i = 0 ; i < N ; i++){
            input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray() ;
            for(int j = 0 ; j < M ; j++){
                lab[i][j] = input[j] ; 
            }
        }
        
        // 1. 벽을 세우고 (완전 탐색 : 모든 경우의 조합 고려)
        build(0, 0, lab, 0) ; 
        System.out.println(max); 
    }
    
    public static void build(int x, int y, int[][] lab, int count){
        if(count == 3){
            // int[][] newLab = Arrays.copyOf(lab) ; --> copyOf 메소드는 1차원 배열에서만 사용 가능
            /*
            [복사 해야하는 이유] 
            배열은 객체의 '참조 값'을 넘겨주는 것이기 때문에 
            메서드 매개변수로 넘어왔더라도 참조하는 실제값을 변경한다.
            즉, 바이러스 퍼지는건 복구 로직이 없기때문에 새로운 배열로 처리해주어야한다.
            (벽 세우기는 복구를 해주기 때문에 원조 배열을 사용해도 괜찮다.)
            */
            // **2차원 배열복사방법 기억**
            int[][] newLab = new int[N][M] ; 
            for(int i = 0 ; i < N ; i++){
                newLab[i] = lab[i].clone() ; 
            }
        
            for(int i = 0 ; i < N ; i++){
                for(int j = 0 ; j < M ; j++){
                    if(newLab[i][j] == 2){
                        spread(i, j, newLab) ; 
                    }
                } 
            }
            count(newLab) ; 
            return ; 
        }
        
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < M ; j++){
                if(lab[i][j] == 0){
                    lab[i][j] = 1 ; 
                    build(i, j, lab, count+1) ; 
                    lab[i][j] = 0 ; 
                }
            } 
        }
    } 
    
    // 2. 바이러스 퍼지기 (Bfs)
    public static void spread(int x, int y, int[][] newLab){
        int[] dx = {-1, 1, 0, 0} ;
        int[] dy = {0, 0, -1, 1} ;
        
        /*
        BFS
        *//*
        Queue<int[]> q = new LinkedList<>() ; 
        q.offer(new int[]{x,y}) ; 
        
        while(!q.isEmpty()){
            int[] start = q.poll() ; 
            for(int i = 0 ; i < 4 ; i++){
                int nx = start[0] + dx[i];
                int ny = start[1] + dy[i];
                
                if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                    continue ; 
                if(newLab[nx][ny]==0){
                    newLab[nx][ny] = 2; 
                    q.offer(new int[]{nx, ny}) ; 
                }
            }
        } */
        /*
        DFS
        */
        for(int i = 0 ; i < 4 ; i++){
            int nx = x + dx[i] ;
            int ny = y + dy[i];
                
            if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                continue ; 
            if(newLab[nx][ny] == 0){
                newLab[nx][ny] = 2;
                spread(nx, ny,newLab) ; 
            }
            
        }
    }
    
    // 3. 안전영역 센 후 최대값 갱신 
    public static void count(int[][] newLab){
        int answer = 0 ; 
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < M ; j++){
                if(newLab[i][j] == 0){
                    answer++ ; 
                }
            } 
        }
        max = Math.max(answer , max) ; 
    }
}
