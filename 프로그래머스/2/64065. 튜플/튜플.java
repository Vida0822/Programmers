import java.util.*; 
class Solution {
    public int[] solution(String s) { // 5 이상 1,000,000
        HashMap<Integer, Integer> map = new HashMap<>() ; 
        String[] tuples = s.split("\\},\\{") ; 
        
        for(String tuple : tuples){ // O(1,000,000) 
            tuple = tuple.replace("{","").replace("}","") ; 
            String[] nums = tuple.split(",") ; 
            
            for(int i = 0 ; i < nums.length ; i++){
                int num = Integer.parseInt(nums[i]) ; 
                map.put(num, map.getOrDefault(num, 0)+1) ; 
            }          
        }
        
        List<Integer> keySet = new ArrayList<>(map.keySet()) ; 
        keySet.sort(new Comparator<Integer>(){
            @Override
            public int compare(Integer o1, Integer o2){
                return map.get(o2).compareTo(map.get(o1)); 
            }
        });
        int[] answer = new int[keySet.size()] ; 
        for(int i = 0 ; i < keySet.size() ; i++){
            answer[i] = keySet.get(i) ; 
        }
        return answer ; 
    }
}