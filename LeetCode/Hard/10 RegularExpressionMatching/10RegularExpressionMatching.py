def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)

    # Lista de listas en vez de vector<vector<bool>>. Se usa una comprensión de listas anidada para crear cada fila de forma independiente (evita el bug clásico de Python donde
    # [[False]*n]*m crea filas que en realidad son la MISMA lista repetida por referencia).
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Fila 0: patrón contra cadena vacía.
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # coincidencia directa, se arrastra el resultado anterior
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                usar_cero = dp[i][j - 2]       # usar X* cero veces
                usar_una_mas = False           # usar X* una vez mas
                caracter_anterior = p[j - 2]
                if caracter_anterior == '.' or caracter_anterior == s[i - 1]:
                    usar_una_mas = dp[i - 1][j]
                dp[i][j] = usar_cero or usar_una_mas
            else:
                dp[i][j] = False

    return dp[m][n]


def main():
    s1, p1 = "aa", "a"
    print(f'Salida del problema 10 ("{s1}", "{p1}"): {is_match(s1, p1)}')

if __name__ == "__main__":
    main()