public class RegularExpressionMatching10 {

    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();

        // boolean[][] en vez de vector<vector<bool>>: es el equivalente directo en Java para una matriz 2D de booleanos.
        // Java inicializa boolean[][] en "false" por defecto automáticamente, igual que el constructor de vector<bool> con valor inicial false.
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;

        // Fila 0: patrón contra cadena vacía.
        for (int j = 1; j <= n; j++) {
            if (p.charAt(j - 1) == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i - 1)) {
                    // coincidencia directa, se arrastra el resultado anterior
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    boolean usarCero = dp[i][j - 2]; // usar X* cero veces
                    boolean usarUnaMas = false;      // usar X* una vez mas
                    char characterAnterior = p.charAt(j - 2);
                    if (characterAnterior == '.' || characterAnterior == s.charAt(i - 1)) {
                        usarUnaMas = dp[i - 1][j];
                    }
                    dp[i][j] = usarCero || usarUnaMas;
                } else {
                    dp[i][j] = false;
                }
            }
        }

        return dp[m][n];
    }

    public static void main(String[] args) {
        RegularExpressionMatching10 sol = new RegularExpressionMatching10();

        String s1 = "aa", p1 = "a";
        System.out.println("Salida del problema 10 (\"" + s1 + "\", \"" + p1 + "\"): " + sol.isMatch(s1, p1));

    }
}