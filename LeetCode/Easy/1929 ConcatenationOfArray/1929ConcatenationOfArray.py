from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1]
    ans = sol.getConcatenation(nums)
    print(ans)