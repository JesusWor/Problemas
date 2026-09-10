def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    # arbitraria de forma nativa, así que no hace falta ningún tipo especial
    # como long long o long para evitar desbordamientos.
    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10  # división entera, equivalente a temp /= 10 en C++/Java

    return reversed_num == x


if __name__ == "__main__":
    x1 = 121
    print(f"x = {x1} -> Es palindromo: {is_palindrome(x1)}")

    x2 = -121
    print(f"x = {x2} -> Es palindromo: {is_palindrome(x2)}")

    x3 = 10
    print(f"x = {x3} -> Es palindromo: {is_palindrome(x3)}")