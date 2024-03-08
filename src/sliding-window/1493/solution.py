from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cuml = [0] * (n + 1)
        cumr = [0] * (n + 1)
        for i in range(n):
            num = nums[i]
            numr = nums[-i-1]
            cuml[i + 1] = num * (cuml[i] + 1)
            cumr[-i -2] = numr * (cumr[-i-1] + 1)

        m = 0
        for i in range(n):
            m = max(m, cuml[i] + cumr[i + 1])

        return m
