from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int, m:int = 1) -> List[List[int]]:

        # no valid solution
        if n < k or n > min(k * 9, 9 * 10 // 2):
            return []

        # valid solution
        if k == 1 and n >= m:
            return [[n]]

        # recursivity
        ans = []
        for i in range(m, 10):
            for sol in self.combinationSum3(k - 1, n - i, i + 1):
                ans.append([i] + sol)

        return ans
