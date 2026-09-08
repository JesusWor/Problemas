def roman_to_int(s: str) -> int:
    # Diccionario en vez de std::map: acceso O(1) promedio, igual que HashMap en Java.
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    length = len(s)
    total = 0
    i = 0

    while i < length:
        # Mismo criterio: si es el último caracter, o el valor actual es
        # mayor o igual que el siguiente -> suma directa y avanza 1.
        if i == length - 1 or roman[s[i]] >= roman[s[i + 1]]:
            num = roman[s[i]]
            i += 1
        else:
            # Caso de sustracción (IV, IX, XL, XC, CD, CM):
            # se suma la diferencia y se avanzan 2 posiciones.
            num = roman[s[i + 1]] - roman[s[i]]
            i += 2
        total += num

    return total


if __name__ == "__main__":
    s = "MCMXCIV"
    print(f"Roman: {s} -> Entero: {roman_to_int(s)}")