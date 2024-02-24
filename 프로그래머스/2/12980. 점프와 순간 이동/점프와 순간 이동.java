import java.util.*;

public class Solution {
    public int solution(int n) {
      
        /*
        알고리즘 : 그리디 
        핵심 아이디어 : 무조건 순간이동을 할 수 있으면 하는게 좋으므로 최종 거리에서 역순으로 계산하면서 2의 배수면 2로 나눠주기 (아니면 어쩔수 없이 배터리 사용 ) --> 위치가 0이 될때까지 매순간 최선의 선택(순간이동)을 하려고 노력하며 줄여주기 
        */
        int k = 0 ; 
        while(n > 0){
            if(n%2 == 0)
                n /= 2 ; 
            else{
                k++ ;
                n-- ;     
            }
        }// while 
        return k ; 
    }
}