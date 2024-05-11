import java.util.* ; 

class Solution { 
    public String solution(int n, int k, String[] cmd) {
        Stack<Integer> remove_order = new Stack<Integer>() ;  
        for(int i = 0 ; i < cmd.length ; i++){
            char c = cmd[i].charAt(0) ; 
            
            if(c == 'D')
                k += Integer.parseInt(cmd[i].substring(2)) ; // 현재 '위치'만 표시함 (실제 그 표를 구현할 필요 없음)
            else if(c=='U')
                k -= Integer.parseInt(cmd[i].substring(2)) ; 
            else if(c == 'C'){
                remove_order.add(k) ; // 제거된 행 번호 추가 
                n-- ; // 테이블 사이즈 감소 
                if(k == n)// 선택된 행이 테이블 사이즈를 벗어나면 
                    k-- ; 
            }else if(c == 'Z'){
                if(remove_order.pop() <= k)
                    k++ ;
                n++ ; 
            }
        }
        
        // Step 2. 답 출력 
        StringBuilder builder = new StringBuilder();
        for(int i = 0 ; i < n; i++)
            builder.append("O");
        while(!remove_order.isEmpty())
            builder.insert(remove_order.pop().intValue(), "X"); 
        	// 스택에서 인덱스 꺼내 해당 위치에 "X"를 삽입. 삭제된 항목이 "O"에서 "X"로 변경
        return builder.toString();
    }
}