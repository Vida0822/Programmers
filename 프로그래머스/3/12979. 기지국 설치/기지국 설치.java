import java.util.*;
class Solution {
    public static int solution(int n, int[] stations, int w)
    {
        int count = 0;
        int state = 0;
        int left = 1;
        int newleft = 0;

        while(true) {
            if(state<stations.length && left >= stations[state] - w) {
                left = stations[state]+w+1;
                state++;
            }
            else {
                newleft = left+w;
                if( (state <= stations.length-2) && (newleft >= stations[state+1]-w))
                    newleft = stations[state+1]-w-1;

                left=newleft+w+1;
                count++;
            }
            if(left > n)
                break;
        }

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        // System.out.println("Hello Java");

        return count;
    }
}