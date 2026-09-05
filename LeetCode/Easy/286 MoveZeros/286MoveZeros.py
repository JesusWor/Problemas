from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1

if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    print(nums)