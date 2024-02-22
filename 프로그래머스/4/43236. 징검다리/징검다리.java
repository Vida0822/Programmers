// 해 자체를 이분탐색 대상으로 삼기 
// 탐색범위 : 바위를 n개 제거한 뒤 각 지점 사이 거리의 최솟값
//      ㄴ 그 최솟값이 될 수 있는 값 중 최댓값이 최종적으로 구하는 값 
// <-> 바위를 n개 제거할 때 가능한 최솟값 중 최댓값 
// 헷갈리는 이유: 최솟값? 최댓값?이 혼용됨
// 탐색 범위 자체는 '최솟값'이고, 그중 허용가능한 최대치가 최종적인 답임
import java.util.* ; 
class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0 ; 
        Arrays.sort(rocks) ;  // 돌이 놓여진 위치 정렬
        
        // 이분 탐색 : 돌을 n개 제거했을 때 지점간 거리 최솟값 
        int left = 1 ;  
        int right = distance ; 
        while(left <= right){
            int mid = (left+right)/2 ; 
            if(getRemovedRockCnt(rocks ,mid, distance)<=n){ // 해당 mid가 답이 되기 위해 돌이 적게 제거 되면 
               
                left = mid + 1 ; // 돌간 최소 거리를 더 크게 잡아서 돌을 더 제거시켜주고  
                 answer = mid ; // 다음 반복에서 해가 안나올 수 있기 때문에 허용 가능 범위일 때 일단 answer에 mid값을 저장해준다 **  
            }else{ // 해당 mid가 답이 되기 위해 돌이 더 많이 제거 되면 
                right = mid -1; // 돌간 최소 거리를 작게 잡아서 돌을 덜 제거해야한다 
            }
        }
        return answer ; 
    }
    public int getRemovedRockCnt(int[] rocks, int mid, int distance){
        // mid 가 바위 지점 간 최소거리가 되기 위해 제거해야할 바위의 수를 return한다 
        // mid가 바위 지점간 최소 거리가 되려면 mid보다 작은 숫자의 거리가 나오면 해당 돌을 제거해야한다 
        // 실제로 돌을 제거하지 않고 제거해야'할' 돌의 갯수를 세는게 포인트 
        int before = 0 ; // 출발지 
        int end = distance ; 
        
        int removeCnt = 0 ; 
        for(int i = 0 ; i < rocks.length ; i++){
            if(rocks[i] - before < mid){
                removeCnt++ ; 
                continue ; 
            }
            before = rocks[i] ; 
        }
        if(end - before < mid) removeCnt++ ; // 마지막 돌과 도착지 사이의 거리(mid보다 짧으면 마지막 돌 제거)
        return removeCnt ; 
    }
}