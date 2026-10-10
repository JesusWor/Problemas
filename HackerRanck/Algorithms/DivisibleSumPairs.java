import java.util.*;

public class DivisibleSumPairs {
    public static int divisibleSumPairs(int n, int k, List<Integer> ar) {
        int contador = 0, suma;
        for (int i=0; i<n-1; i++){
            for(int j=i+1; j<n; j++) {
                suma = ar.get(i) + ar.get(j);
                System.out.println("i: " + i + " j: " + j + " suma: " + suma);
                if(suma % k == 0) {
                    System.out.println("Cuenta");
                    contador++;
                }
            }
        }
        return contador;
    }
    public static void main(String[] args) {
        int n = 6, k = 3;
        List<Integer> ar = new ArrayList<>();
        ar.add(1);
        ar.add(3);
        ar.add(2);
        ar.add(6);
        ar.add(1);
        ar.add(2);
        System.out.println(divisibleSumPairs(n, k, ar));
    }
}
