from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    resultado = sol.runningSum(nums)
    print(resultado)