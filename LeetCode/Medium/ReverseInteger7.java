public class ReverseInteger7{
    public static int reverse(int x) {
        int reversed = 0;
        while( x != 0) {
            int digit = x % 10;

            if(reversed > Integer.MAX_VALUE / 10 || reversed < Integer.MIN_VALUE/10){
                return 0;
            }
            reversed = reversed * 10 + digit;
            x /= 10;
        }
        return reversed;
    }
    
    public static void main(String[] args) {
        System.out.println(reverse(123));
        System.out.println(reverse(456));
        System.out.println(reverse(-123));
    }
}