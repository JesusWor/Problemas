import java.util.*;
import java.util.stream.Stream;

public class BetweenTwoSets {
    public static int getTotalX(List<Integer> a, List<Integer> b) {
        if (a == null || b == null || a.isEmpty() || b.isEmpty()) {
            return 0;
        }
        int maxA = a.stream().max(Integer::compareTo).orElse(Integer.MIN_VALUE);
        int minB = b.stream().min(Integer::compareTo).orElse(Integer.MAX_VALUE);
        int contador = 0;
        for (int i = maxA; i <= minB; i++) {
            boolean numeroValido = true;

            for (int numa : a) {
                if (i % numa != 0) {
                    numeroValido = false;
                    break;
                }
            }

            if (numeroValido) {
                for (int numb : b) {
                    if (numb % i != 0) {
                        numeroValido = false;
                        break;
                    }
                }
            }

            if (numeroValido) {
                contador++;
            }
        }
        return contador;
    }

    public static void main(String[] args) {
        List<Integer> a = Arrays.asList(2, 4);
        List<Integer> b = Arrays.asList(16, 32, 96);
        System.out.println(getTotalX(a, b));

        List<Integer> a2 = Arrays.asList(3, 4);
        List<Integer> b2 = Arrays.asList(24, 48);
        System.out.println(getTotalX(a2, b2));
    }
}
