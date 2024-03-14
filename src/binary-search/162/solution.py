from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            m = (j + i) // 2
            before = nums[m - 1] if m > 0 else float('-inf')
            after = nums[m + 1] if m < len(nums) - 1 else float('-inf')
            mid = nums[m]
            if before < mid and mid > after:
                break
            else:
                if before > mid:
                    j = m
                else:
                    i = m + 1
                continue

        return (i + j) // 2

