class Solution:
    def isPalidrome(self, s: str) -> bool:
        filtered = "".join([c.lower() for c in s if c.isalnum()])
        reversed_str = filtered[::-1]

        return filtered == reversed_str

def main():
    sol = Solution()

    # Saida esperada ejemplo 1: True
    s = "A man, a plan, a canal: Panama"
    print("Salida ejemplo 1: ", sol.isPalidrome(s))

    # Saida esperada ejemplo 2: True
    s = " "
    print("Salida ejemplo 2: ", sol.isPalidrome(s))

if __name__ == "__main__":
    main()

