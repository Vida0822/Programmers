import java.util.*;
class Solution {
    Map<String, PriorityQueue<String>> graph = new HashMap<>();
    public String[] solution(String[][] tickets) {
        for(String[] ticket : tickets){
            String key = ticket[0];
            if(!graph.containsKey(key)){
                graph.put(key, new PriorityQueue<>());
            }
            graph.get(key).offer(ticket[1]);
        }

        return dfs("ICN").toArray(new String[0]);
    }

    private Deque<String> dfs(String key){
        if(!graph.containsKey(key) || graph.get(key).isEmpty()){
            return new LinkedList<>(List.of(key));
        }

        Deque<String> right = dfs(graph.get(key).poll());
        if(!graph.get(key).isEmpty()){
            Deque<String> left = dfs(graph.get(key).poll());
            if(left.size() > right.size()){
                while(!right.isEmpty()){
                    left.addLast(right.pollFirst());
                }
                right = left;
            } else {
                while(!left.isEmpty()){
                    right.addFirst(left.pollLast());
                }
            }
        }
        right.addFirst(key);
        return right;
    }
}