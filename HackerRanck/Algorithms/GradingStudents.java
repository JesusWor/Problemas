import java.io.*;
import java.math.*;
import java.util.*;

class GradingStudents {
    public static List<Integer> gradingStudents(List<Integer> grades) {
        List<Integer> ans = new ArrayList<Integer>();
        
        for (int i=0; i<grades.size(); i++) {
            int j = grades.get(i);
            if (j < 38){
                ans.add(j);
            }
            else {
                int nextmult = ((j / 5) + 1) * 5;
                if (nextmult - j < 3) {
                    ans.add(nextmult);
                } else {
                    ans.add(j);
                }
            }
        }
        
        return ans;
    }
    public static void main(String[] args) throws IOException {
        List<Integer> prueba = new ArrayList<>();
        prueba.add(73);
        prueba.add(67);
        prueba.add(38);
        prueba.add(33);

        List<Integer> resultado = gradingStudents(prueba);
        System.out.println(resultado);
    }
}
