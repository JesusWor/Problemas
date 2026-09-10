#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    bool isMatch(std::string s, std::string p) {        
        int m = s.length(), n = p.length();
        std::vector<std::vector<bool>> dp (m+1, std::vector<bool>(n+1, false));
        dp[0][0] = true;
        
        // Fila 0: patrón contra cadena vacía. Solo puede ser true, si el patrón es una secuencia de "X*" (ej: "a*b*c*")
        for(int j=1; j<=n; j++) {
            if(p[j-1] == '*') {
                dp[0][j] = dp[0][j-2];
            }
        }

        for(int i=1; i<=m; i++) {
            for(int j=1; j<=n; j++) {
                if(p[j-1] == '.' || p[j-1] == s[i-1]) {
                    dp[i][j] = dp[i-1][j-1]; // coincidencia directa por lo que arrastro el resultado anterior;
                } else if(p[j-1] == '*') {
                    bool usarCero = dp[i][j-2]; // usar X* cero veces
                    bool usarUnaMas = false; // usar X* una vez mas 
                    char characterAnterior = p[j-2];
                    if(characterAnterior == '.' || characterAnterior == s[i-1]) {
                        usarUnaMas = dp[i-1][j];
                    }
                    dp[i][j] = usarCero || usarUnaMas;
                } else {
                    dp[i][j] = false;
                }
            }
        }
        return dp[m][n];
    }
};

int main() {
    Solution sol;
    std::string s = "aa",
                p = "a";
    std::cout<<"Salida del problema 10: "<<sol.isMatch(s,p)<< std::endl;
}