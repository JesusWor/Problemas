class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        max_len = 0
        i = 0
        j = 0
        n = len(s)

        while j < n:
            if s[j] not in st:
                st.add(s[j])
                j += 1
                max_len = max(max_len, len(st))
            else:
                st.remove(s[i])
                i += 1

        return max_len

if __name__ == "__main__":
    sol = Solution()
    cadena = "abcabcbb"
    resultado = sol.lengthOfLongestSubstring(cadena)
    print(resultado)