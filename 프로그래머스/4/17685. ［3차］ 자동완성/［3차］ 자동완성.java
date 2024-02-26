import java.util.HashMap;
import java.util.Map;

class Solution {

    public class Node {
        Map<Character, Node> child = new HashMap<>(); // 특정 문자의 자식 노드들을 저장하는 HashMap 
        Node before = null; // 부모 계층 노드 
        Boolean isEnd = false; // leaf 노드인지 확인 
    }

    public class Trie {
        public Node root = new Node(); // 루트 노드 생성 (특정 문자 x)

        public void insert(String input) { // 특정 문자열을 노드들로 넣어준다 
            Node node = this.root; // 빈 기준 노드를 가져와서 첫번째 계층 노드로 설정 

            for (int i = 0; i < input.length(); i++) {
                Node before = node; // 이전 문자 노드를 before에 넣어주고 
                node = node.child.computeIfAbsent(input.charAt(i), k -> new Node());
                node.before = before;
            }

            node.isEnd = true;
        }

        //각 단어의 최소 입력 횟수 계산
        public int calInputCnt(String input) {
            Node node = this.root;

            //마지막 노드로 이동
            for (int i = 0; i < input.length(); i++) {
                node = node.child.getOrDefault(input.charAt(i), null);
            }

            //1. 마지막 노드가 leaf 노드가 아닐 경우
            if (node.child.size() != 0) return input.length();

            //2. 마지막 노드가 leaf 노드일 경우
            int cnt = 0;
            while(true) {
                node = node.before;
                if (node == null) {
                    cnt--;
                    break;
                }
                if (node.isEnd == false && node.child.size() == 1)
                    cnt++;
                else
                    break;
            }
            return input.length() - cnt;
        }
    }

    public int solution(String[] words) {
        Trie trie = new Trie();
        //트라이 입력
        for (int i = 0; i < words.length; i++)
            trie.insert(words[i]);

        //각 단어의 최소 입력 횟수 계산
        int result = 0;
        for (int i = 0; i < words.length; i++) {
            result += trie.calInputCnt(words[i]);
        }
        return result;
    }
}