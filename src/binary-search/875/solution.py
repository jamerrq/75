from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cost(k):
            return sum([ceil(x / k) for x in piles])

        i = 1
        j = max(piles)
        while i < j:
            mid = (i + j) // 2
            tmp = cost(mid)
            #
            if tmp > h:
                i = mid + 1

            else:
                j = mid

        return i
