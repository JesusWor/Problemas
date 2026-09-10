def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    separation = num_rows - 2
    n = len(s)
    resultado = []

    for i in range(num_rows):
        j = i
        while j < n:
            resultado.append(s[j])
            if i == 0 or i == num_rows - 1:
                j += (2 * separation + 2)
            else:
                j += (2 * separation + 2)
                if j - (2 * i) < n:
                    resultado.append(s[j - (2 * i)])

    return "".join(resultado)


def main():
    s = "PAYPALISHIRING"
    num_rows = 3
    print(convert(s, num_rows))


if __name__ == "__main__":
    main()