from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        cache = {}
        for num in nums:
            if cache.get(k - num, 0):
                cache[k - num] -= 1
                ans += 1
            else:
                cache[num] = cache.get(num, 0) + 1

        return ans
