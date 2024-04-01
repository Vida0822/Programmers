import java.util.* ; 
class Solution {
    public int[] solution(int[] progresses, int[] speeds) { // n = 100
        int n = progresses.length ; 
        
        // 남은 작업일수로 queue 만들기 
        Queue<Integer> q = new LinkedList<>(); 
        for(int i = 0 ; i < n ; i++){
            int leftDay = (100-progresses[i])/speeds[i]  ;
            if((100-progresses[i])%speeds[i]  > 0)
                leftDay+=1 ; 
            q.offer(leftDay) ; 
        }
        
        // 맨 앞 작업이 배포될때 함께 배포될 수 있는 뒷작업들 확인 (남은 일수가 더 적어야 함) 
        ArrayList<Integer> workdays = new ArrayList<>();
        while(!q.isEmpty()){
            int count = 1 ;
            int leftDay = q.poll() ;
            while(!q.isEmpty() && q.peek() <= leftDay){
                q.poll() ; 
                count ++ ;
            }
            workdays.add(count) ; 
        }
        
        // 동적배열 --> 정적배열 변환 (답 형식 맞추기) 
        int[] answer = new int[workdays.size()] ; 
        for(int i = 0 ; i < workdays.size() ; i++){
            answer[i] = workdays.get(i) ; 
        }
        return answer ; 
    }
}