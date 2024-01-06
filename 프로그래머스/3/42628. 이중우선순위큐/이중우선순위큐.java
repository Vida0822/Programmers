import java.util.* ; 

class Solution {
    public int[] solution(String[] operations) {
        
        List<Integer> queue = new LinkedList<Integer>() ; 
        int[] answer = new int[2] ; 
        
        for(String o : operations){
            String[] temp = o.split(" ") ; 

            String operation = temp[0] ; 
            int operand = Integer.parseInt(temp[1]) ; 
            
            if(operation.equals("I")){ // 여기서 '==' 쓰면 오류 ! (== 는 String에선 참조를 비교하는 것)
                queue.add(operand) ; 
                queue.sort(Comparator.naturalOrder()) ; 
            } else if(queue.size() > 0 && operation.equals("D")){
                if(operand == 1){
                    queue.remove(queue.size()-1) ;
                }else{
                    queue.remove(0) ; 
                }
            }           
        } // for
        if(queue.size() == 0){
            answer[0] = answer[1] = 0 ;         
        }else{         
            answer[0] = queue.get(queue.size()-1) ; 
            answer[1] = queue.get(0) ;
        }
        return answer ; 
    } // solution 
} // class