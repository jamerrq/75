from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        aux = sum(nums[:k])
        curr = aux / k
        ans = curr
        for i in range(k, len(nums)):
            aux += nums[i] - nums[i - k]
            curr = aux / k
            ans = max(ans, curr)

        return ans
