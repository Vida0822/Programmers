import java.util.*;
class Snake{
    int x ; 
    int y ;
    
    public Snake(int x, int y){
        this.x = x ; 
        this.y = y ; 
    }
}

public class Main{
    public static int[][] board ; 
    public static int N ; 
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        N = sc.nextInt(); 
        board = new int[N][N] ; 
        
        // 사과 채우기 
        int K = sc.nextInt() ; 
        for(int i = 0 ; i < K ; i++){
            int x = sc.nextInt() -1 ; 
            int y = sc.nextInt() -1 ; 
            board[x][y] = 1 ; 
        }
        
        // 회전 정보 채우기 
        int L = sc.nextInt() ; 
        HashMap<Integer,String> timetable = new HashMap<>() ; 
        for(int i = 0 ; i < L ; i++){
            int x = sc.nextInt(); 
            String c = sc.next() ; 
            timetable.put(x, c) ; 
        }
        
        // 뱀 이동하기 
        int answer = 0 ; 
        Queue<Snake> q = new LinkedList<>() ; 
        q.add(new Snake(0,0)) ; 
        board[0][0] = 2 ; 
        
        int[] dx = {0, 1 , 0, -1} ;  // 동남서북
        int[] dy = {1, 0, -1, 0} ; 
        int x = 0 , y = 0 , d = 0 ; 
        
        while(true){
            answer++ ; 
            int nx = x+dx[d] ;
            int ny = y+dy[d] ; 
            
            // 해당 좌표에 뱀이 있거나, 벽이 있으면 return false
            if(nx < 0 || ny < 0 || nx >= N || ny >= N)
                break ; 
            if(board[nx][ny] == 2)
                break ; 
            
            // 사과가 있으면 해당 좌표만 2로 변경, 없으면 꼬리쪽 2 빼고 머리쪽 2 등록  
            if(board[nx][ny] == 0){
                Snake snake = q.poll() ; 
                board[snake.x][snake.y] = 0 ; 
            }
            board[nx][ny] = 2 ; 
            q.add(new Snake(nx,ny)) ; 
            
            // 방향 전환 (X초가 '끝난 뒤' 회전)
            if(timetable.containsKey(answer)){
                String dir = timetable.get(answer); 
                
                if(dir.equals("D"))
                    d = (d+1 == 4? 0 : d+1);
                else
                    d = (d-1 == -1? 3 : d-1);
            }
            x = nx ; 
            y = ny ;           
        }
        System.out.println(answer); 
    }
}