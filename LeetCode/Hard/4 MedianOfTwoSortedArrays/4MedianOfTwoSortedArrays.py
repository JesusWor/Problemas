from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        merged = []
        i = j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < m:
            merged.append(nums1[i])
            i += 1

        while j < n:
            merged.append(nums2[j])
            j += 1

        total = m + n
        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            return (merged[total // 2 - 1] + merged[total // 2]) / 2.0

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]

    mediana = sol.findMedianSortedArrays(nums1, nums2)
    print(mediana)