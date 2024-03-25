import java.util.*; 
class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>() ; 
        for(int i = 0 ; i < clothes.length ;i++){
            String type = clothes[i][1] ; 
            map.put(type, map.getOrDefault(type,0) + 1) ; 
        }
        int answer = 1 ; 
        for(String type : map.keySet()){
            int count = map.get(type) ; 
            answer *= (count+1) ; 
        }
        return answer -1 ;
    }
}