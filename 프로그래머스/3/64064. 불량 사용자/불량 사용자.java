import java.util.* ; 
class Solution {
    static HashSet<HashSet<String>> answer  = new HashSet<>() ; 
    // 경우의 수 목록 <<경우의 수1>,<경우의 수2>,<경우의 수3>>
    // 경우의 수 : 아이디들의 집합 <아이디1, 아이디2, 아이디3> 
    static String[] user_id ; 
    static String[] banned_id ; 
    
    public int solution(String[] user_id, String[] banned_id) {
        
        this.user_id = user_id ; 
        this.banned_id = banned_id ; 
         
        dfs(new LinkedHashSet<>()) ; 
        return answer.size() ; 
    }// solution
    
    private static void dfs(HashSet<String> hs){ // hs 현재까지 선택된 user_id의 집합
        // 종료 조건 
        if(hs.size() == banned_id.length){ // 선택된 user_id의 갯수가 ban 대상 id의 갯수와 일치할 때 
            if(isBanList(hs, banned_id)) // hs가 유효한 조합인지 확인하고 
                answer.add(new HashSet<>(hs)) ; // 경우의 수 목록에 추가  
            return ; 
        }
        
        // 인접 노드 방문 
        for(String userId : user_id){ // user_id를 하나씩 검사하면서 
            if(hs.add(userId)){
                dfs(hs) ; 
                hs.remove(userId) ; 
            }
        }
    }
      private static boolean isBanList(HashSet<String> hs, String[] banned_id) {
        int idx = 0;
        for (String userID : hs) {
            String banID = banned_id[idx++];
            
            if (userID.length() != banID.length()) { // user_id와 ban_id의 길이가 같아야함 
                return false;
            }
            for (int i = 0; i < banID.length(); i++) { // ban_id와 한글자씩 비교하면서 
                if (banID.charAt(i) == '*') { // ban_id의 글자가 '*'이면 
                    continue; 
                }
                if (userID.charAt(i) != banID.charAt(i)) { // 글자가 다르면 
                    return false; // ban_id가 아니다 
                }
            }
        }
        return true;
    }
}