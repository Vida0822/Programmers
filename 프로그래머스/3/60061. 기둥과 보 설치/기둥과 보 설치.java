import java.util.*; 

class Node implements Comparable<Node>{
    int x ; 
    int y ; 
    int stuff ; 
    
    public Node(int x, int y, int stuff){
        this.x = x ; 
        this.y = y ; 
        this.stuff = stuff ; 
    }
    
    @Override 
    public int compareTo(Node other){
        if(this.x == other.x && this.y == other.y)
            return Integer.compare(this.stuff, other.stuff) ; 
        if(this.x == other.x)
            return Integer.compare(this.y, other.y) ; 
        return Integer.compare(this.x , other.x) ; 
    }
}

class Solution{
    
    public int[][] solution(int n, int[][] build_frame){
        ArrayList<ArrayList<Integer>> answer = new ArrayList<ArrayList<Integer>>() ; 
        
        for(int i = 0 ; i < build_frame.length ; i++){
            int x = build_frame[i][0] ; 
            int y = build_frame[i][1] ; 
            int stuff = build_frame[i][2]  ;
            int operate = build_frame[i][3] ; 
            
            if(operate == 0){
                int index = 0 ; 
                for(int j = 0 ; j < answer.size() ; j++){
                    if(x == answer.get(j).get(0) && y == answer.get(j).get(1) && stuff == answer.get(j).get(2))
                        index = j ; 
                }
                ArrayList<Integer> erased = answer.get(index ) ; 
                answer.remove(index) ; 
                if(!possible(answer))
                    answer.add(erased) ; // 그 객체 그대로 설치 
                
            }else{
                ArrayList<Integer> inserted = new ArrayList<Integer>() ; 
                inserted.add(x) ; 
                inserted.add(y) ; 
                inserted.add(stuff) ; 
                answer.add(inserted) ; 
                if(!possible(answer))
                    answer.remove(answer.size()-1) ; 
            }
                
        }
        ArrayList<Node> ans = new ArrayList<Node>() ; 
        for(int i = 0 ; i < answer.size() ; i++)
            ans.add(new Node(answer.get(i).get(0), answer.get(i).get(1) , answer.get(i).get(2))) ; 
        Collections.sort(ans) ; 
        
        int[][] res = new int[ans.size()][3];
        for (int i = 0; i < ans.size(); i++) {
            res[i][0] = ans.get(i).x;
            res[i][1] = ans.get(i).y;
            res[i][2] = ans.get(i).stuff;
        }
        return res;
    }
    
    public boolean possible(ArrayList<ArrayList<Integer>> answer){
        for(int i = 0 ; i < answer.size() ; i++){
            int x = answer.get(i).get(0) ; 
            int y = answer.get(i).get(1) ; 
            int stuff = answer.get(i).get(2) ; 
            
            if(stuff == 0){
                boolean check = false ; 
                
                if(y == 0)
                    check = true ; 
                
                // 보의 한쪽 끝 위 또는 다른 기둥 위라면 성상 
                for(int j = 0 ; j < answer.size() ; j++){
                    if(1 == answer.get(j).get(2) && 
                       x-1 == answer.get(j).get(0) && 
                        y == answer.get(j).get(1))
                        check = true ; 
                    if(1 == answer.get(j).get(2) &&
                      x == answer.get(j).get(0) && 
                      y == answer.get(j).get(1))
                        check = true ; 
                    if(0 == answer.get(j).get(2) &&
                      x == answer.get(j).get(0) && 
                      y-1 == answer.get(j).get(1))
                        check = true ; 
                }     
            if(!check) return false ; 
        }else if(stuff == 1){
            boolean check = false ; 
            boolean left = false ; 
            boolean right = false ; 
            
            for(int j = 0 ; j < answer.size() ; j++){
                if( 0 == answer.get(j).get(2) && 
                   x == answer.get(j).get(0) && 
                  y-1 == answer.get(j).get(1)) 
                    check = true ; 
                if( 0 == answer.get(j).get(2) && 
                   x+1 == answer.get(j).get(0) && 
                  y-1 == answer.get(j).get(1)) 
                    check = true ; 
                
                if(1 == answer.get(j).get(2) && 
                   x-1 == answer.get(j).get(0) && 
                  y == answer.get(j).get(1))
                    left = true ;
                
                if(1 == answer.get(j).get(2) &&
                  x+1 == answer.get(j).get(0) && 
                  y == answer.get(j).get(1))
                    right = true ; 
                }
            if(left && right) check = true ; 
            if(!check) return false ; 
            }
        
        }
        return true ; 
    }
}