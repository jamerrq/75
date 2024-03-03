from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        ans = 0
        while i < j:
            hi = height[i]; hj = height[j]
            w = j - i
            h = min(hi, hj)
            ans = max(w * h, ans)
            if hi > hj:
                j -= 1
            else:
                i += 1

        return ans
