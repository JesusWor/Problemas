import java.util.HashSet;

public class LongestSubstringWithoutRepeatingCharacters3 {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int maxLen = 0;
        int i = 0;
        int j = 0;
        int n = s.length();
        
        while (j < n) {
            if (!set.contains(s.charAt(j))) {
                set.add(s.charAt(j));
                j++;
                maxLen = Math.max(maxLen, set.size());
            } else {
                set.remove(s.charAt(i));
                i++;
            }
        }
        return maxLen;
    }

    public static void main(String[] args) {
        LongestSubstringWithoutRepeatingCharacters3 sol = new LongestSubstringWithoutRepeatingCharacters3();
        String s = "abcabcbb";
        int resultado = sol.lengthOfLongestSubstring(s);
        System.out.println(resultado);
    }
}