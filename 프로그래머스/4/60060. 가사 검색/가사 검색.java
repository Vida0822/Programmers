import java.util.* ; 
class Solution {
    class Trie{
        // 필드 
        Map<Integer,Integer> lenMap = new HashMap<>() ; 
        Trie[] child = new Trie[26] ; 
        
        // 메서드
        void insert(String str){
            // 
            Trie node = this; 
            int len = str.length() ; 
            lenMap.put(len, lenMap.getOrDefault(len,0)+1) ; 
            // 한글자씩 Trie에 삽입 
            for(char ch : str.toCharArray()){
                int idx = ch-'a' ; 
                if(node.child[idx] == null)
                    node.child[idx] = new Trie() ; 
                
                node = node.child[idx] ; 
                node.lenMap.put(len, node.lenMap.getOrDefault(len,0)+1); 
            }
        } // insert 
        
        int find(String str, int i){
            if(str.charAt(i) == '?')
                return lenMap.getOrDefault(str.length(), 0) ; 
            int idx = str.charAt(i) - 'a' ; 
            return child[idx] == null? 0 : child[idx].find(str, i+1) ; 
        } // find 
    } // Trie
    
    public int[] solution(String[] words, String[] queries) {
        Trie front = new Trie() ; 
        Trie back = new Trie() ; 
        /*
        역방향 Trie를 만드는 이유 : queries에서 첫글자가 '?'면 ?를 자식으로 갖는 Trie를 만들기 힘들어서?? 
        */
        // 후보 단어들 Trie에 삽입 (insert)
        for(String word : words){
            front.insert(word);  
            back.insert(reverse(word)) ; 
        }
        
        // queries에 매치되는 단어들 찾기 
        return Arrays.stream(queries).mapToInt(
            query -> query.charAt(0) == '?' ?
                    back.find(reverse(query),0) : 
                    front.find(query,0)).toArray() ; 
}
    String reverse(String s){
        return new StringBuilder(s).reverse().toString() ; 
    }
}