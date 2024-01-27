import java.util.* ; 
class Solution {
    public int solution(int n) {
         int postPattern = n & -n, smallPattern = ((n ^ (n + postPattern)) / postPattern) >> 2;
        return n + postPattern | smallPattern;
    }
}
