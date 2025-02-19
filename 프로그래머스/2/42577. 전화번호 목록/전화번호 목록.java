import java.util.* ; 

class Solution {
    public static int N ; 
    public boolean solution(String[] phone_book) { 
        // N < 1,000,000 --> O(N^2) 이하, 전화번호 길이 < 20  
        // 어떤 번호가 다른 번호의 접두어인 경우 
        N = phone_book.length ; 
        HashSet<String> keys = new HashSet<>() ; 
        
        /*
        for(String number : phone_book){ //O(Nx20)
            StringBuilder sb =  new StringBuilder(); 
            for(int i = 0 ; i < number.length()-1 ; i++){
                sb.append(number.charAt(i)) ; 
                keys.add(sb.toString()) ; 
            }
        }         
        for(int i = 0 ; i < N ; i++){ // O(N)
            if(keys.contains(phone_book[i])) 
                    return false;
        }
        */
        // 접두어를 key로 끼는게 아닌, 단어를 key로 끼고 접두어가 해당 key를 포함하는지 확인 
        for(String word : phone_book){ // O(N)
            keys.add(word) ; 
        }
        for(String number : phone_book){ //O(Nx20)
            StringBuilder sb =  new StringBuilder(); 
            for(int i = 0 ; i < number.length()-1 ; i++){
                sb.append(number.charAt(i)) ; 
                if(keys.contains(sb.toString()))
                    return false; 
            }
        }
        
        
        return true; 
        
        
        
    }
}