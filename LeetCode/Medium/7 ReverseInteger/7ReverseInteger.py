def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1   # 2147483647
    INT_MIN = -2**31      # -2147483648
    sign = -1 if x < 0 else 1
    x = abs(x)

    reversed_num = 0
    while x != 0:
        digit = x % 10
        if reversed_num > INT_MAX // 10:
            return 0

        reversed_num = reversed_num * 10 + digit
        x //= 10

    reversed_num *= sign

    # Verificacion final de rango (por el signo aplicado al final):
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0

    return reversed_num

def main():
    print(reverse(123))
    print(reverse(456))
    print(reverse(-123))
    print(reverse(1534236469)) 

if __name__ == "__main__":
    main()