import java.util.* ; 
class Work implements Comparable<Work>{
    int request ; 
    int work ; 
    
    public Work(int request , int work){
        this.request = request ; 
        this.work = work ; 
    }
    @Override 
    public int compareTo(Work other){
        return this.work-other.work; 
    }
}

class Solution {
    
    public static int answer = 0 ;  
    public static int endTime = 0 ; 
    public static PriorityQueue<Work> pq = new PriorityQueue<>() ; 
    public static boolean[] done ;  
    
    public int solution(int[][] jobs) {
        // 우선순위 큐를 사용해 가장 작업시간이 짧은걸 꺼내서 작업한다 
        // 반복문 변수 : time 
        
        Arrays.sort(jobs, new Comparator<int[]>(){
            @Override
            public int compare(int[] job1, int[] job2){
                if(job1[0] != job2[0])
                    return job1[0] - job2[0] ; 
                return job1[1] - job2[1] ; 
            }
        }) ; 
        // 두개의 우선순위를 가짐 - 1. 요청 시간 , 2. 요청 순서 
        
        
       // int done = 1 ;      

        // 작업이 모두 완료될 때 까지 
        done = new boolean[jobs.length] ; 
        done[0] = true ; 
        pq.add(new Work(jobs[0][0] , jobs[0][1])) ; 
        bfs(jobs) ; 
        
        for(int i = 0 ; i < done.length ; i++){
            if(!done[i]){
                done[i] = true; 
                pq.add(new Work(jobs[i][0], jobs[i][1])) ; 
                bfs(jobs) ; 
            }
        }
        return answer / jobs.length ; 
    }
    
    
    public void bfs(int[][] jobs){
        while(!pq.isEmpty()){
            Work work = pq.poll() ; // 작업 수행 
            
            // 요청 시간 ~ 요청 종료 소요시간 add 
            if(work.request > endTime)
                endTime = work.request + work.work ; 
            else 
                endTime += work.work ;  // 이전 task 마감시간 + 작업시간 = 최종 작업 종료시간 
            answer += endTime - work.request ;  // 소요 시간 = 작업 종료시간 - 요청시간   
            System.out.println(work.request + " " + endTime)  ;     
            
            for(int i = 0 ; i < jobs.length ; i++){
                if(done[i])
                    continue; 
                if(jobs[i][0] < endTime){
                    done[i] = true ; 
                    pq.add(new Work(jobs[i][0], jobs[i][1])) ; 
                }
            }
        }
    }
}