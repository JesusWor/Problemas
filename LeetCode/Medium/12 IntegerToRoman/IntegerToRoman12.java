import java.util.List;
import java.util.Map;
import java.util.AbstractMap.SimpleEntry;

public class IntegerToRoman12 {

    public String intToRoman(int num) {
        // Lista de pares (valor, símbolo) ordenada de mayor a menor,
        // igual que el vector<pair<int,string>> en C++.
        // Se usa List<Map.Entry<...>> porque Java no tiene un "pair" nativo
        // como C++; SimpleEntry es la forma estándar de simular un par.
        List<Map.Entry<Integer, String>> val = List.of(
            new SimpleEntry<>(1000, "M"), new SimpleEntry<>(900, "CM"),
            new SimpleEntry<>(500, "D"),  new SimpleEntry<>(400, "CD"),
            new SimpleEntry<>(100, "C"),  new SimpleEntry<>(90, "XC"),
            new SimpleEntry<>(50, "L"),   new SimpleEntry<>(40, "XL"),
            new SimpleEntry<>(10, "X"),   new SimpleEntry<>(9, "IX"),
            new SimpleEntry<>(5, "V"),    new SimpleEntry<>(4, "IV"),
            new SimpleEntry<>(1, "I")
        );

        // StringBuilder en vez de concatenar String directamente:
        // concatenar strings con += en un ciclo es O(n^2) en Java
        // porque String es inmutable y cada += crea un nuevo objeto;
        // StringBuilder evita eso y es la práctica estándar.
        StringBuilder ans = new StringBuilder();

        for (Map.Entry<Integer, String> pair : val) {
            while (num >= pair.getKey()) {
                ans.append(pair.getValue());
                num -= pair.getKey();
            }
        }

        return ans.toString();
    }

    public static void main(String[] args) {
        IntegerToRoman12 sol = new IntegerToRoman12();
        int num = 3749; // salida esperada "MMMDCCXLIX"
        String salida = sol.intToRoman(num);
        System.out.println("Salida: " + salida);
        System.out.println(salida.equals("MMMDCCXLIX"));
    }
}