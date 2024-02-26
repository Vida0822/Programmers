import java.util.* ; 

class Food implements Comparable<Food>{
    private int index ; // 음식 번호 
    private int time ;  // 먹방시간
    
    public Food(int index, int time){
        this.index = index ; 
        this.time = time ; 
    }
    public int getIndex(){return this.index ; }
    public int getTime() {return this.time ; }
    
    @Override
    public int compareTo(Food other){
        return Integer.compare(this.time, other.getTime()) ; 
    }
}
class Solution{
    public int solution(int[] food_times, long k){
        
        // 총 먹방 시간이 k보다 적은 경우 
        long sumTime = 0 ; 
        for(int i = 0 ; i < food_times.length ; i++){
            sumTime+= food_times[i] ; 
        }
        if(sumTime <= k)
            return -1 ; 
        
        // 적은 먹방시간을 가진 음식 반환 
        PriorityQueue<Food> pq = new PriorityQueue<>() ; 
        for(int i = 0 ; i < food_times.length; i++){
            pq.offer(new Food(i+1 , food_times[i])) ; 
        }
        sumTime = 0 ; // 최종적인 누적 먹방 진행 시간 
        long previous = 0 ;  // 이미 흐른 시간  
        long length = food_times.length ; // 음식 갯수 
        
        while(sumTime + (pq.peek().getTime()-previous)*length <= k){ // 만약 최소시간음식을 기준으로 모든 음식을 먹었을 때 total 누적 방송시간이 방송 중단시간 k를 초과한다면 해당 turn은 돌리지 않는다
            int now = pq.poll().getTime() ; // 해당 음식 먹방시간
            sumTime += (now - previous)*length ;  // 이전에 고려해준 먹방시간은 이미 지난것으로 처리해줘야하므로 총 누적먹방시간을 갱신해줄 땐 '(이 음식을 먹는데 걸리는 시간 - 이미 흐른 먹방시간)* 음식 갯수'를 해줘야한다.   
            previous = now ; // 이미 흐른 시간
            length -- ; // 음식 하나는 다 먹어 없앴으므로
        }
        
        //순차탐색 : pq에 남은 음식을 순차적으로 먹는 도중 방송이 중단될것 (도중 다 먹는 음식은 없다) --> 중단되는 시점을 구해서 음식번호 반환 
       
        // 음식번호순으로 정렬 
        ArrayList<Food> result = new ArrayList<>() ; 
        while(!pq.isEmpty()){
            result.add(pq.poll()) ; 
        }
        result.sort(Comparator.comparing(Food::getIndex)) ; // 암기 
        
        long turn = (k-sumTime) // 중단시점까지 남은 시간을 ex) 17 
            % length ; // 음식 종류로 나눈 나머지는 중단되는 시점 : 음식 종류수는 변하지 않으므로 이게 가능  ex) 8 
        int foodNum = result.get((int)turn) // 중단 시점에 먹을 음식의 
            .getIndex() ; // 음식번호 
        return foodNum ;  // 반환
        
        
    }
}