import java.util.* ; 
class Solution {
    
    public int[] parent ; 
    public int find(int i){
        if(parent[i] == i)
            return i ; 
        else return parent[i] = find(parent[i]) ; 
    } 
    
    public void union(int a, int b){
        int parent_a = find(a) ; // a의 부모 
        int parent_b = find(b) ; // b의 부모 
        
        // 1 1 1 5 5 
        // 1 2 3 4 5 
        if(parent_a != parent_b)
            // parent[b] = parent_a ; --> b가 속한 집합의 루트를 a의 부모로 설정 (b원소를 a로 이동 ; a와 b는 다른 집합)
            parent[parent_b]  // parent[find(b)] b의 루트
            = parent_a ; 
        // b가 속한 집합의 루트 자체를 a로 변경  
    }
    
    public int solution(int n, int[][] costs) {
        
        // part 1. 초기 상태
        parent = new int[n] ; 
        for(int i = 0 ; i < n ; i++){
            parent[i] = i ; 
        }
        
        // part 2. 가중치 기준으로 정렬 
        Arrays.sort(costs,  (o1, o2) -> o1[2] - o2[2]) ; 
        
        // part 3. 최소 신장 비용 구하기 
        int answer = 0 ; 
        for(int i = 0 ; i < costs.length ; i++){
            if(find(costs[i][0]) != find(costs[i][1])){
                union(costs[i][0], costs[i][1]) ; 
                answer += costs[i][2] ; 
            }
        }
        return answer ; 
    } // solution 
} // class 