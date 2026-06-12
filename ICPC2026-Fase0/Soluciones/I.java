import java.util.*;

public class I {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<String> enchants = new ArrayList<>();

        for (int i=0; i<n; i++) {
            enchants.add(sc.next());
        }
        String secret = sc.next();
        sc.close();

        String magicString = recursiveStart(enchants, secret);
        System.out.print(magicString + "\n");
        System.out.print(magicString.equals("") ? "NO" : "YES");

    }

    static String recursiveStart(List<String> enchants, String secret) {
        for (String enchant : enchants) {
            for (int i = 0; i < enchant.length(); i++) {
                String s = enchant.substring(i);

                if (secret.startsWith(s)) {
                    String result = recursive(enchants, secret.substring(s.length()), enchant);
                    if (!result.equals("")) return result;
                }

                if (s.startsWith(secret)) {
                    return enchant;
                }
            }
        }

        return "";
    }

    static String recursive(List<String> enchants, String secret, String current) {
        if (secret.length() == 0) return current;

        for (String s : enchants) {
            if (secret.startsWith(s)) {
                String result = recursive(enchants, secret.substring(s.length()), current + s);
                if (!result.equals("")) return result;
            }

            if (s.startsWith(secret)) {
                return current + s;
            }
        }

        return "";
    }
}



