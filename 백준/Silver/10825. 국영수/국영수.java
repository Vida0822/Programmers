import java.util.* ;
import java.io.* ; 

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ; 
        int N = Integer.parseInt(br.readLine()) ; 
        
        Student[] students = new Student[N] ; 
        for(int i = 0 ; i < N ; i++){
            String[] input = br.readLine().split(" ") ; 
            students[i] = new Student(input[0], Integer.parseInt(input[1]),Integer.parseInt(input[2]),Integer.parseInt(input[3])) ; 
        }
        Arrays.sort(students) ; 
        for(int i = 0 ; i < N ; i++){
            Student s = students[i] ; 
            System.out.println(s.getName()) ; 
        }
    }
}
class Student implements Comparable<Student>{
    String name ; 
    int kor ; 
    int eng ; 
    int mat ; 
    // 편의상 getter, setter 생략

    public Student(String name, int kor, int eng , int mat){   
        this.name = name ; 
        this.kor = kor ; 
        this.eng = eng ; 
        this.mat = mat ; 
    }
    public String getName(){
        return this.name ; 
    }
    
    @Override
    public int compareTo(Student other){
        if(this.kor != other.kor)
            return other.kor - this.kor ; 
        
        if(this.eng != other.eng)
            return this.eng - other.eng ; 
        
        if(this.mat != other.mat)
            return other.mat - this.mat ; 
        
        return this.name.compareTo(other.name);
        
    }
}