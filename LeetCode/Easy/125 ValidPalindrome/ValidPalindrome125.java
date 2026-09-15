public class ValidPalindrome125 {
    public boolean isPalindrome(String s){
        StringBuilder filtered = new StringBuilder();

        for(char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                filtered.append(Character.toLowerCase(c));
            }
        }
        String filteredStr = filtered.toString();
        String reversedStr = new StringBuilder(filteredStr).reverse().toString();

        return filteredStr.equals(reversedStr);
    }

    public static void main(String[] args) {
        ValidPalindrome125 sol = new ValidPalindrome125();

        String s = "A man, a plan, a canal: Panama";
        System.out.println("Salida ejemplo 1: " + sol.isPalindrome(s));

        s = " ";
        System.out.println("Salida ejemplo 1: "+sol.isPalindrome(s));

    }
}
