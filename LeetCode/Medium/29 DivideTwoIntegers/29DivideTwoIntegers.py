def divide(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = False
    dvs = divisor
    dvd = dividend

    if dvs < 0:
        dvs = -dvs
        negative = not negative
    if dvd < 0:
        dvd = -dvd
        negative = not negative

    ans = 0
    while dvd >= dvs:
        temp, multiple = dvs, 1
        while dvd >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dvd -= temp
        ans += multiple

    result = -ans if negative else ans

    return max(INT_MIN, min(INT_MAX, result))


def main():
    print("Prueba de salida 1:", divide(10, 3))    # esperado 3
    print("Prueba de salida 2:", divide(7, -3))     # esperado -2
    print("Prueba de salida 3:", divide(-2147483648, -1))  # esperado INT_MAX


if __name__ == "__main__":
    main()