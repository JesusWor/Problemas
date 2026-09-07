from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1
        return water

if __name__ == "__main__":
    sol = Solution()
    alturas = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    resultado = sol.trap(alturas)
    print(resultado)