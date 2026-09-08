import java.util.HashMap;
import java.util.Map;

public class RomanToInteger13 {

    public int romanToInt(String s) {
        // HashMap en vez de map ordenado de C++: aquí no necesitamos orden,
        // solo acceso rápido O(1) por clave, igual que el map de C++ (que es O(log n)
        // por ser árbol balanceado; HashMap mejora eso a O(1) promedio).
        Map<Character, Integer> roman = new HashMap<>();
        roman.put('I', 1);
        roman.put('V', 5);
        roman.put('X', 10);
        roman.put('L', 50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);

        int len = s.length();
        int sum = 0;
        int i = 0;

        while (i < len) {
            int num;
            // Mismo criterio que en C++: último carácter, o el actual
            // vale igual o más que el siguiente -> suma directa.
            if (i == (len - 1) || roman.get(s.charAt(i)) >= roman.get(s.charAt(i + 1))) {
                num = roman.get(s.charAt(i));
                i++;
            } else {
                // El actual vale menos que el siguiente -> caso de sustracción (IV, IX, XL, etc.)
                num = roman.get(s.charAt(i + 1)) - roman.get(s.charAt(i));
                i += 2;
            }
            sum += num;
        }
        return sum;
    }

    public static void main(String[] args) {
        RomanToInteger13 sol = new RomanToInteger13();
        String s = "MCMXCIV";
        System.out.println("Roman: " + s + " -> Entero: " + sol.romanToInt(s));
    }
}