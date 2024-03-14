from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            iftake = dp[i - 2] if i > 1 else 0
            ignore = dp[i - 1]
            dp[i] = max(iftake + nums[i], ignore)


        return dp[-1]
