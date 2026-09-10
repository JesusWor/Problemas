public class PalindromeNumber9 {

    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        // long en vez de long long: Java no tiene "long long", su tipo
        // long ya es de 64 bits (equivalente al long long de 64 bits en C++),
        // así que cubre el mismo propósito: evitar overflow al invertir el número.
        long reversed = 0;
        long temp = x;

        while (temp != 0) {
            int digit = (int) (temp % 10);
            reversed = reversed * 10 + digit;
            temp /= 10;
        }

        return (reversed == x);
    }

    public static void main(String[] args) {
        PalindromeNumber9 sol = new PalindromeNumber9();

        int x1 = 121;
        System.out.println("x = " + x1 + " -> Es palindromo: " + sol.isPalindrome(x1));

        int x2 = -121;
        System.out.println("x = " + x2 + " -> Es palindromo: " + sol.isPalindrome(x2));

        int x3 = 10;
        System.out.println("x = " + x3 + " -> Es palindromo: " + sol.isPalindrome(x3));
    }
}