import java.util.* ; 
class Solution {
    public int solution(int[][] routes) {
        /*
        사용 로직 
        : 이어져있지 않은 부분을 기준으로 그룹을 나눠 각각 감시 카메라를 설치한다 
        1) 각 차를 순서대로 고려 
        2) 차의 진입지점이 그룹의 최대 진출지점보다 더 갔을 때 new 그룹 
        3) 차의 진출지점이 그룹의 최소 진입지점보다 덜 갔을 때 new 그룹 
        4) 그룹이 겹칠 땐 최소 진입지점, 최대 진출지점 갱신 
        5) 그룹 갯수만큼 감시 카메라 설치 
        */
        
        ArrayList<Car> list = new ArrayList<>() ; 
        for(int i = 0 ; i < routes.length ; i++){
            Car car = new Car(routes[i][0], routes[i][1]) ; 
            list.add(car) ; 
        } // for 
        
        // 2. 
        Collections.sort(list, (a,b) -> {  // 비교하는 두 Car 
            return Integer.compare(a.out, b.out) ; // 진출 시점으로 정렬 
        }) ; 
            
        // 3. 
        boolean[] included = new boolean[list.size()] ; 
        // 해당 차가 감시카메라 영역에 포함되었는지 여부 
        
        int group = 0 ; 
        for(int i = 0 ; i < list.size() ; i++){
            if(included[i]) 
                continue ; 
            
            group++ ; 
            // 해당 그룹에 포함되는 차들 검사 
            for(int j = i+1 ; j < list.size(); j++){
                if(list.get(i).out >= list.get(j).in){
                    // 해당 그룹의 최대 진출 시점 이전에 차의 진입 시점이 우선하면 
                    included[j] = true ; // 해당 차는 감시카메라에 속함 
                } // if 
            } // j             
        } // i
        return group ; 
    } // solution 
} // class 

class Car{
    int in ; 
    int out ; 
    
    public Car(int in, int out){
        this.in = in ; 
        this.out = out ; 
    }
}
