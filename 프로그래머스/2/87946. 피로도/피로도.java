import java.util.*; 
class Dungeon{
    int need ; 
    int use ; 
    
    public Dungeon(int need, int use){
        this.need = need ; 
        this.use = use; 
    }
}
class Solution {
    public static int answer = 0 ; 
    public int solution(int k, int[][] dungeons) {
        // 규칙성이 있는가? 
        // 없다면 모든 순열을 구해서 max 값을 반환해야함 
        // ---> ㅇ : dungeons 길이가 8로 매우 작기 때문에 여러번 순열을 구해도 된다
        // 순열 구하기 : dfs -> 해당 순열로 탐험가능한 던전수 구하기 -> max 갱신 
        Stack<Dungeon> list = new Stack<>() ; 
        boolean[] visited = new boolean[dungeons.length] ; 
        dfs(k, dungeons, list, visited) ; 
        return answer ;
    }
    
    public static void dfs(int k, int[][] dungeons, Stack<Dungeon> list, boolean[] visited){
        if(list.size() == dungeons.length){
            
            answer = Math.max(answer, possibleCount(k, list) ); 
        }
        for(int i = 0 ; i < dungeons.length ; i++){
            if(visited[i]) 
               continue ;
            visited[i] = true ; 
            list.push(new Dungeon(dungeons[i][0], dungeons[i][1])) ;  
            dfs(k, dungeons,list, visited); 
            
            visited[i] = false ;
            list.pop() ; 
        }
    }
    
    public static int possibleCount(int k, Stack<Dungeon> list){
        int count = 0 ; 
        for(Dungeon dungeon : list){
            if(k < dungeon.need)
                break ;
            count++ ; 
            k -= dungeon.use; 
        }
        return count ; 
    }
}