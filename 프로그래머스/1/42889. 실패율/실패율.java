import java.util.* ; 

class Stage implements Comparable<Stage>{
    int index ;
    double failRatio ; 
    
    public Stage(int index, double failRatio){
        this.index = index ;
        this.failRatio = failRatio ; 
    }
    
    @Override
    public int compareTo(Stage other){
        if(this.failRatio > other.failRatio)
            return -1 ;
        else if(this.failRatio < other.failRatio)
            return 1 ;
        else 
            return this.index - other.index ; 
    }
}

class Solution {
    public int[] solution(int N, int[] stages) {
        // 전체 스테이지의 수 N (1 ~ 500) 
        // 각 사용자가 멈춰있는 스테이지 번호 배열 : stages (~200000)
        
        Arrays.sort(stages) ; 
        boolean[] visited = new boolean[N+1] ; 
        int people = stages.length ;
        
        PriorityQueue<Stage> stopStages = new PriorityQueue<>() ; 
        // 실패율이 0이상인 스테이지 TreeMap에 저장 
        for(int i = 0 ; i < stages.length ; i++){
            int stopAt = stages[i] ; // 3 
            int count = 1; 
            while(i+count != stages.length && stopAt == stages[i+count] ){
                count ++ ; 
            }
            if(stopAt <= N){
                stopStages.offer(new Stage(stopAt, (double)count/(people-i))) ; 
                visited[stopAt] = true ; 
            }
            i+=count -1 ; 
        }
        
        
        // TreeMap에 정렬된 순서대로 stage번호 넣기 
        ArrayList<Integer> list = new ArrayList<>() ; 
        while (!stopStages.isEmpty()) { 
            Stage stage = stopStages.poll() ; 
            if(!list.contains(stage.index))
                list.add(stage.index) ; 
        }
                
        // TreeMap에 없는 stage들 stage번호순으로 넣기 
        for(int i = 1 ; i <= N ; i++){
            if(!visited[i])
                list.add(i) ; 
         }
        
        // 배열로 변환
        int[] answer = new int[N] ; 
        for(int i = 0 ; i < list.size() ; i++){
            answer[i] = list.get(i) ;
        }
        return answer ;
        
    }
}