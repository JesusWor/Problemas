def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix_chars = []
    first = strs[0]

    for i in range(len(first)):
        ch = first[i]

        for s in strs:
            if i >= len(s) or ch != s[i]:
                return "".join(prefix_chars)

        prefix_chars.append(ch)

    return "".join(prefix_chars)


def main():
    ejemplo1 = ["flower", "flow", "flight"]
    print(f'Prefijo comun: "{longest_common_prefix(ejemplo1)}"')


if __name__ == "__main__":
    main()