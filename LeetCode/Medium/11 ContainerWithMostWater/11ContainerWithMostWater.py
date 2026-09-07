from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            ancho = r - l
            alto = min(height[r], height[l])
            area = ancho * alto
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    alturas = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    resultado = sol.maxArea(alturas)
    print(resultado)