from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        R = sum(nums)
        L = 0
        for i in range(len(nums)):
            if L == R - nums[i]:
                return i
            L += nums[i]
            R -= nums[i]

        return -1
