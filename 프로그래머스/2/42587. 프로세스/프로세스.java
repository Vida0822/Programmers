import java.util.* ; 

class Solution {
    public int solution(int[] priorities, int location) {
        
         // 우선순위가 높은 순으로 정렬된 큐 
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder()) ; 
        for(int i = 0 ; i < priorities.length ; i++){
            pq.offer(priorities[i]) ; 
        }
        
        int answer = 1 ; 
         while (!pq.isEmpty()) {
            // 기존 우선순위 배열 순회
            for (int i = 0; i < priorities.length; i++) {
                // 현재 작업의 위치 찾기
                if (pq.peek() == priorities[i]) { // 가장 우선순위가 높은 작업과 i 번째 작업의 우선순위가 동일하다면
                    if (location == i) // 대상 작업이 location 번째 작업이면 
                        return answer;
                    
                    pq.poll(); // 아니면 실행하고 
                    answer++; // 실행 차례 증가       
                }
            }
        }
        return answer ; 
    }
}