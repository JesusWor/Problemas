public class DivideTwoIntegers29 {

    public int divide(int dividend, int divisor) {
        // Unico caso que desborda int: INT_MIN / -1
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        boolean negative = false;
        long dvs = divisor;
        long dvd = dividend;
        long ans = 0;

        if (divisor < 0) {
            dvs = -dvs;
            negative = !negative;
        }
        if (dividend < 0) {
            dvd = -dvd;
            negative = !negative;
        }

        while (dvd >= dvs) {
            long temp = dvs, multiple = 1;
            // busca la mayor potencia de 2 tal que dvs*2^k quepa en dvd
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            ans += multiple;
        }

        return (int) (negative ? -ans : ans);
    }

    public static void main(String[] args) {
        DivideTwoIntegers29 sol = new DivideTwoIntegers29();

        // Salida esperada: 3
        System.out.println("Prueba de salida 1: " + sol.divide(10, 3));

        // Salida esperada: -2
        System.out.println("Prueba de salida 2: " + sol.divide(7, -3));

        // Caso de saturacion: salida esperada Integer.MAX_VALUE
        System.out.println("Prueba de salida 3: " + sol.divide(-2147483648, -1));
    }
}