import java.util.*; 
class Solution {
    public int[] solution(String msg) {
        /*
        초기화 (1번)
        */
        HashMap<String, Integer> map = new HashMap<>() ; 
        int i ; 
        for(i = 0; i <= 26; i++){
            String key = (char)(i+64) +"" ; 
            map.put(key, i) ; 
        }
        
        
        /*
        반복 (2~4번)
        */
        ArrayList<Integer> list = new ArrayList<>() ; 
        // 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        // <-> 해당 검색 키워드와 일치하는 값이 있으면, 해당 index 저장 후 다음 글자 합치기 
        // 다음 합친 글자도 일치값이 있으면 index 갱신 
        // 만약 없으면, 기존 index값 답에 add & 해당 합친 글자값으로 사전에 추가
        // 검색 단어 다음 글자로 초기화 
        // 문자열 끝에 도달하면 반복 종료
        int index = 0 ;
        String search = "" ; 
        for(int j = 0 ; j < msg.length() ; j++){
            search += msg.charAt(j) ; 
            if(map.containsKey(search)){
                index = map.get(search) ; 
            }else{
                list.add(index) ; 
                map.put(search, i++) ;
                search = "" ; 
                j--;
            }
        }
        if(search!="")
            list.add(index) ; 
        
        /*
        답 반환 : list -> array
        */
        int[] answer = new int[list.size()] ; 
        for(int k = 0 ; k < list.size() ; k++){
            answer[k] = list.get(k) ; 
        }
        return answer ; 
    }
}