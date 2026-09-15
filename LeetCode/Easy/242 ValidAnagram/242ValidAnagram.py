class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n,m= len(s),len(t)
        if n!=m:
            return False

        Hmapa = {}
        # meter s en el mapa caracter por caracter
        for idx, letra in enumerate(s):
            Hmapa[letra] = idx

        for c in t:
            if c not in Hmapa or Hmapa[c] == 0:
                return False
            Hmapa[c] -= 1

        return True

def main():
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    print("Salida ejemplo 1: ", sol.isAnagram(s,t))

    s = "rat"
    t = "car"
    print("Salida ejemplo 1: ", sol.isAnagram(s,t))


if __name__ == "__main__":
    main()