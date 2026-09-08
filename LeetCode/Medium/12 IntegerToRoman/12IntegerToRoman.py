def int_to_roman(num: int) -> str:
    # Lista de tuplas (valor, símbolo), equivalente al vector<pair<int,string>>.
    # Python tiene tuplas nativas, así que no hace falta ninguna clase auxiliar.
    val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),  (1, "I")
    ]

    ans = []  # Lista de strings en vez de concatenar directamente
    for value, symbol in val:
        while num >= value:
            ans.append(symbol)
            num -= value

    return "".join(ans)


if __name__ == "__main__":
    num = 3749  # salida esperada "MMMDCCXLIX"
    salida = int_to_roman(num)
    print(f"Salida: {salida}")
    print(salida == "MMMDCCXLIX")