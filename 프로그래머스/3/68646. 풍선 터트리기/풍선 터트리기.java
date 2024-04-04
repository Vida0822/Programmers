class Solution {
    public int solution(int[] a) {
        // n = 1000000 --> should be in O(N)  
        if(a.length == 1) return 1; // possible 
        if(a.length == 2) return 2 ; // both possible 
        
        int leftMin = a[0] ; 
        int[] rightMin = new int[a.length] ; 
        rightMin[a.length-1] = a[a.length-1] ; 
    
        // point : exception is only allowed for examining element(a[i]) --> At both sides of a[i] would remain the minimum number from each sides' numbers   
        for(int i = a.length -2 ; i > 0 ;i--)
            rightMin[i] = Math.min(rightMin[i+1], a[i]) ; // rightMin[i] : minimun number in a[i] ~ a[end]
        
        int count = 0 ; 
        // Two-pointer & Regurality 
        for(int i = 0 ; i < a.length ;i++){
            if(!(leftMin < a[i] && rightMin[i] < a[i] )) // except only when minumums of both size are smaller than a[i] (than should pop smaller bollunes twice) 
                count++; 
            leftMin = Math.min(leftMin, a[i]) ;
            // leftMin : minumum number in a[0] ~ a[i] 
        }
        return count; 
    }
}