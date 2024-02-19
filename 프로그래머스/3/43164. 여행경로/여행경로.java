import java.util.*; 

class Solution {
    public static HashMap<String, ArrayList<String>> graph ; 
    public static ArrayList<String> path = new ArrayList<>() ; 
    
    public String[] solution(String[][] tickets) {
        // part 1. 그래프 만들기 
        graph = new HashMap<>() ; 
        for(int i = 0 ; i < tickets.length ; i++) {
            String from = tickets[i][0];
            String to = tickets[i][1];
            if(!graph.containsKey(from))
                graph.put(from, new ArrayList<>()) ; 
            graph.get(from).add(to);
        }
        
        // 도착지를 알파벳 순서로 정렬
         Collections.sort(graph.values(), new Comparator<Stack<String>>() {
                @Override
                public int compare(Stack<String> o1, Stack<String> o2) {
                    for (int i = 0; i < o1.size(); i++) {
                        String s1 = o1.get(i);
                        String s2 = o2.get(i);

                        if (!s1.equals(s2)) {
                            return s1.compareTo(s2);
                        }
                    }

                    return 0;
                }
            });
        
        // part 2. dfs 수행 + 이동 경로 기록 
        dfs("ICN", tickets.length) ; 
        
        // part 3. 경로 반환 
        String[] answer = path.toArray(new String[0]) ;
        return answer ; 
    }
    
    public static boolean dfs(String airport, int ticketsLeft){
        path.add(airport) ; 
         
        if(ticketsLeft == 0) // 모든 티켓을 사용했을 때
            return true;
        
        ArrayList<String> destinations = graph.get(airport) ; 
        if(destinations == null)
            return false; 
        
        for(int i = 0; i < destinations.size(); i++){
            String nextAirport = destinations.get(i);
            destinations.remove(i); // 사용한 티켓 제거
            
            if(dfs(nextAirport, ticketsLeft - 1)) // 재귀 호출
                return true;
            
            destinations.add(i, nextAirport); // 백트래킹
        }
        
        // 티켓을 모두 사용하지 않은 경우
        path.remove(path.size() - 1);
        return false;
    }
}
