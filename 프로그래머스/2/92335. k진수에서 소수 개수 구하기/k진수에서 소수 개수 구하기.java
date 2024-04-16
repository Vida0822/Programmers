class Solution {
    public int solution(int n, int k) {
        // n -> k 
        // n = 1,000,000...so big - O(N) 
            
        // 1. transform n --> k's n (method 1)
        String s = transform(n, k) ; 
        
        // 2. count sosu... (method 2 )
        return getCount(s) ; 
    }
    
    public static String transform(int n, int k){
        
        StringBuilder ts = new StringBuilder() ; 
        while(n != 0){
            ts.insert(0, n%k) ; 
            n /= k ; 
        }
        return ts.toString() ; 
    }
    
    public static int getCount(String s){
    //    System.out.println(s.replaceAll("0", "#")) ; 
        String[] nums = s.split("0") ; 
        int count = 0 ; 
        
        for(String num : nums){
           if(num.equals(""))
                continue; 
            //System.out.print(num+" ") ; 
            long d = Long.parseLong(num );
            if(checkDecimal(d))
                count++ ; 
        }
        return count ; 
    }
    
    public static boolean checkDecimal(long num){  
        if(num==1)
            return false; 
        
        long a = (long)Math.sqrt(num) + 1; 

        // 3~ 
        for(int i = 2 ; i < a ; i++){
            if (num % i == 0) 
                return false;
        }
        return true; 
    }
}