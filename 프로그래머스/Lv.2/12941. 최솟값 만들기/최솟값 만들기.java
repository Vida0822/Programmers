import java.util.* ; 
class Solution{
    /*
    [사용한 로직]
    : 큰값을 최대한 작은값과 곱해 누적해줘야 최솟값이 나온다 
    => 각 배열을 정렬한 후 반대방향으로 서로 곱해준다  
    */
    public int solution(int []A, int []B) {
        Arrays.sort(A) ; 
        Arrays.sort(B) ; 
        
        int sum = 0 ;
        int len = A.length ; 
        for(int i = 0 ; i < len ; i++){
            sum += A[i] * B[len-i-1] ;  // A배열은 앞에서부터, B배열은 뒤에서부터 곱해줌 
        }
        // 1 2 4 / 4 4 5 
        return sum;
    }
}