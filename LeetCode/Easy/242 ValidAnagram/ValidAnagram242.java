import java.util.HashMap;

public class ValidAnagram242 {
    public boolean isAnagram(String s, String t) {
        int n=s.length(), m=t.length();
        if(n!=m) {
            return false;
        }
        HashMap<Character, Integer> mapa = new HashMap<>();

        // meter s en un hashmap 
        for(char c:s.toCharArray()){
            mapa.put(c, mapa.getOrDefault(c, 0) + 1);
        }
        // Comparar que la letra de t esté en el mapa
        for(char c:t.toCharArray()) {
            // si la letra que se esta comparando no existe o ya se usaron todas las letras regresa false
            if(!mapa.containsKey(c) || mapa.get(c) == 0) {
                return false;
            }
            // decrementar el contador en el mapa
            mapa.put(c, mapa.get(c)-1);
        }

        return true;
    }

    public static void main(String[] args){
        ValidAnagram242 sol = new ValidAnagram242();
        String s = "anagram", 
               t = "nagaram";
        // Salida esperada: true;
        System.out.println("Salida ejemplo 1: " + sol.isAnagram(s,t));

        s = "rat";
        t = "car";
        // Salida esperada: false;
        System.out.println("Salida ejemplo 2: " + sol.isAnagram(s,t));
    }
}
