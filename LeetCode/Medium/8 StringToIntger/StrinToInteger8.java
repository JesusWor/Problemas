public class StrinToInteger8{
    public static int myAtoi(String s) {
        int i = 0, n = s.length(), sign = 1, result = 0;

        // Delete spaces
        while(i<n && s.charAt(i) == ' '){
            i++;
        }
        
        // Sign checking
        if(i<n && (s.charAt(i) == '+' || s.charAt(i) == '-')){
            sign = (s.charAt(i) == '-') ? -1 : 1;
            i++;
        }

        // Convert
        while (i<n && Character.isDigit(s.charAt(i))){
            int digit = s.charAt(i) - '0';
            if(result > Integer.MAX_VALUE / 10 ||
            (result == Integer.MAX_VALUE / 10 && digit > 7)){
                return (sign==1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            result = result * 10 + digit;
            i++;
        }
        return result * sign;
    }

    public static void main(String[] args) {
        System.out.println(myAtoi("42"));
        System.out.println(myAtoi("   -042"));
        System.out.println(myAtoi("1337c0d3"));
        System.out.println(myAtoi("0-1"));
        System.out.println(myAtoi("words and 987"));    
    }
}