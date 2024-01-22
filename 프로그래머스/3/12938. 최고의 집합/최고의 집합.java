import java.util.* ; 

class Solution {
    public int[] solution(int n, int s) {
        
        if(n > s){ // 구성 자연수 갯수인 n이 합계 s보다 작으면 
            return new int[]{-1} ; 
        }   
        int[] answer = new int[n] ; // 구성 자연수 갯수인 n만큼의 배열 생성 
        /*
        사용한 수학적 원리 
        : 각 원소의 곱이 최대가 되려면 각 요소가 평균의 근사치여야함 
        */
        int avg = s/n ; // 각각의 요소를 평균값으로 설정하고 (이때 나머지가 탈락함)
        int rest = s - avg*n ;  // 실제 합계보다 모자란 만큼을 rest 로 설정 
        for(int i = 0 ; i < n ; i++){ // 각 요소 하나하나를 돌면서 
            if(rest != 0){ // rest 값이 남아있으면 
                answer[i] = avg+1 ; // 평균에 1을 더함 
                rest -- ; // rest 값 감소 
            }else{
                answer[i] = avg ; // rest 값이 없으면 그대로 평균 삽입 
            }            
        }
        Arrays.sort(answer); // 정렬 후 return 
        return answer ; 
    } // solution
} // class