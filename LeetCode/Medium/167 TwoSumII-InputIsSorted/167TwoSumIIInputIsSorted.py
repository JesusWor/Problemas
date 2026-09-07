from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum_target = numbers[i] + numbers[j]
            if sum_target == target:
                return [i + 1, j + 1]
            elif sum_target < target:
                i += 1
            else:
                j -= 1
        return []

if __name__ == "__main__":
    sol = Solution()
    numeros = [2, 7, 11, 15]
    objetivo = 9
    resultado = sol.twoSum(numeros, objetivo)
    print(resultado)