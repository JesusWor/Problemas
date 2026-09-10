import java.util.List;

public class LongestCommonPrefix14 {

    public String longestCommonPrefix(List<String> strs) {
        if (strs.isEmpty()) {
            return "";
        }

        StringBuilder prefix = new StringBuilder();
        String first = strs.get(0);

        for (int i = 0; i < first.length(); i++) {
            char ch = first.charAt(i);

            for (String s : strs) {
                if (i >= s.length() || ch != s.charAt(i)) {
                    return prefix.toString();
                }
            }

            prefix.append(ch);
        }

        return prefix.toString();
    }

    public static void main(String[] args) {
        LongestCommonPrefix14 sol = new LongestCommonPrefix14();

        List<String> ejemplo1 = List.of("flower", "flow", "flight");
        System.out.println("Prefijo comun: \"" + sol.longestCommonPrefix(ejemplo1) + "\"");

        List<String> ejemplo2 = List.of("dog", "racecar", "car");
        System.out.println("Prefijo comun: \"" + sol.longestCommonPrefix(ejemplo2) + "\"");

        List<String> ejemplo3 = List.of("interspecies", "interstellar", "interstate");
        System.out.println("Prefijo comun: \"" + sol.longestCommonPrefix(ejemplo3) + "\"");
    }
}