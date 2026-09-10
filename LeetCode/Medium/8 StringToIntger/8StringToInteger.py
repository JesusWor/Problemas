def my_atoi(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    i, n, sign, result = 0, len(s), 1, 0

    # salta espacios en blanco iniciales
    while i < n and s[i] == ' ':
        i += 1

    # detecta signo opcional, una sola vez
    if i < n and s[i] in ('+', '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # acumula digitos consecutivos, se detiene en el primer no-digito
    while i < n and s[i].isdigit():
        digit = int(s[i])
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + digit
        i += 1

    return result * sign

def main():
    print(my_atoi("42"))
    print(my_atoi("   -042"))
    print(my_atoi("1337c0d3"))
    print(my_atoi("0-1"))
    print(my_atoi("words and 987"))

if __name__ == "__main__":
    main()